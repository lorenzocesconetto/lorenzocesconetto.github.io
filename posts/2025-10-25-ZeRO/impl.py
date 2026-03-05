import torch
import torch.distributed as dist


class ZeRO_1:
    def __init__(self, model, optimizer_cls):
        self.model = model
        self.rank = dist.get_rank()
        self.world_size = dist.get_world_size()

        self.param_metadata = []
        shard_list = []

        for param in self.model.parameters():
            original_shape = param.data.shape
            flat = param.data.view(-1)
            numel = flat.numel()

            remainder = numel % self.world_size
            pad_size = (self.world_size - remainder) % self.world_size
            padded_numel = numel + pad_size
            shard_size = padded_numel // self.world_size

            shard_start = self.rank * shard_size
            shard_end = shard_start + shard_size

            self.param_metadata.append(
                {
                    "original_shape": original_shape,
                    "numel": numel,
                    "padded_numel": padded_numel,
                    "shard_size": shard_size,
                    "shard_start": shard_start,
                    "shard_end": shard_end,
                }
            )

            if pad_size > 0:
                flat_padded = torch.cat([flat, flat.new_zeros(pad_size)])
            else:
                flat_padded = flat

            shard = flat_padded[shard_start:shard_end].clone()
            shard_list.append(shard)

        self.param_shards = [s.requires_grad_(True) for s in shard_list]
        self.optimizer = optimizer_cls(self.param_shards)

    def training_step(self, inputs, targets, loss_fn):
        output = self.model(inputs)
        loss = loss_fn(output, targets)
        loss.backward()

        self._sync_gradients()  # all-reduce gradients across GPUs
        self.optimizer.step()
        self._allgather_params()

        # clear gradients for the next step
        for param in self.model.parameters():
            param.grad = None

    def _sync_gradients(self):
        for idx, param in enumerate(self.model.parameters()):
            meta = self.param_metadata[idx]

            dist.all_reduce(param.grad, op=dist.ReduceOp.SUM)
            param.grad /= self.world_size

            self.param_shards[idx].grad = param.grad.view(-1)[
                meta["shard_start"] : meta["shard_end"]
            ]

    def _allgather_params(self):
        for idx, param in enumerate(self.model.parameters()):
            meta = self.param_metadata[idx]

            full_flat = torch.empty(meta["padded_numel"], device=param.device, dtype=param.dtype)
            dist.all_gather_into_tensor(
                output_tensor=full_flat,
                input_tensor=self.param_shards[idx].data,
            )

            param.data.copy_(full_flat[: meta["numel"]].view(meta["original_shape"]))


class ZeRO_2(ZeRO_1):
    def _sync_gradients(self):
        """
        ZeRO-2: reduce_scatter gradients so each rank receives only
        the averaged gradient shard for the parameters it owns,
        saving gradient memory by 1/world_size vs ZeRO-1.
        """
        for idx, param in enumerate(self.model.parameters()):
            meta = self.param_metadata[idx]

            # Pad the gradient to match padded_numel, same as we do for params
            grad_flat = param.grad.view(-1)
            pad_size = meta["padded_numel"] - meta["numel"]
            if pad_size > 0:
                grad_flat = torch.cat([grad_flat, grad_flat.new_zeros(pad_size)])

            # Each rank receives only its own shard of the reduced gradient
            grad_shard = torch.zeros(meta["shard_size"], device=param.device, dtype=param.dtype)
            dist.reduce_scatter_tensor(
                output=grad_shard,
                input=grad_flat.contiguous(),
                op=dist.ReduceOp.SUM,
            )
            grad_shard /= self.world_size

            self.param_shards[idx].grad = grad_shard


class ZeRO_3(ZeRO_2):
    """
    ZeRO-3: Shard optimizer states (stage 1) + gradients (stage 2) + model parameters (stage 3).

    At rest, each rank holds only param_shards[idx] — a 1/world_size slice
    of each parameter. Full parameters are materialised temporarily during
    the forward and backward passes via all_gather, then immediately freed.
    """

    def __init__(self, model, optimizer_cls):
        self.model = model
        self.rank = dist.get_rank()
        self.world_size = dist.get_world_size()

        self.param_metadata = []
        shard_list = []

        self._param_to_idx = {}

        for idx, param in enumerate(self.model.parameters()):
            original_shape = param.data.shape
            flat = param.data.view(-1)
            numel = flat.numel()

            remainder = numel % self.world_size
            pad_size = (self.world_size - remainder) % self.world_size
            padded_numel = numel + pad_size
            shard_size = padded_numel // self.world_size

            shard_start = self.rank * shard_size
            shard_end = shard_start + shard_size

            self.param_metadata.append(
                {
                    "original_shape": original_shape,
                    "numel": numel,
                    "padded_numel": padded_numel,
                    "shard_size": shard_size,
                    "shard_start": shard_start,
                    "shard_end": shard_end,
                }
            )

            if pad_size > 0:
                flat_padded = torch.cat([flat, flat.new_zeros(pad_size)])
            else:
                flat_padded = flat

            shard = flat_padded[shard_start:shard_end].clone()
            shard_list.append(shard)

            # Replace the full tensor with only this rank's shard.
            # The model's param.data now points to a tiny slice; the full
            # weight will be reconstructed on demand during forward/backward.
            param.data = shard.detach()
            self._param_to_idx[param] = idx

        self.param_shards = [s.requires_grad_(True) for s in shard_list]
        self.optimizer = optimizer_cls(self.param_shards)

        self._register_hooks()

    def _gather_param(self, idx, device, dtype):
        """All-gather the full parameter tensor for parameter `idx`."""
        meta = self.param_metadata[idx]
        full_flat = torch.empty(meta["padded_numel"], device=device, dtype=dtype)
        dist.all_gather_into_tensor(
            output_tensor=full_flat,
            input_tensor=self.param_shards[idx].data,
        )
        return full_flat[: meta["numel"]].view(meta["original_shape"])

    def _allgather_all_params(self):
        """Temporarily restore full params into model.parameters() for a fwd/bwd pass."""
        for idx, param in enumerate(self.model.parameters()):
            param.data = self._gather_param(idx, param.device, param.dtype)

    def _reshard_module_params(self, module):
        """Reshard params back to local shard for every direct param of this module."""
        for param in module.parameters(recurse=False):
            idx = self._param_to_idx[param]
            param.data = self.param_shards[idx].data

    def training_step(self, inputs, targets, loss_fn):
        # 1. All-gather full params before the forward pass
        self._allgather_all_params()

        output = self.model(inputs)
        loss = loss_fn(output, targets)

        # 2. Backward needs full params too; they're still materialised here.
        loss.backward()

        # 3. Reduce-scatter gradients (ZeRO-2 logic, inherited)
        self._sync_gradients()

        # 4. Free full params — each rank holds only its shard again
        self._reshard_all_params()

        # 5. Each rank updates only its local shard; no communication needed
        self.optimizer.step()

        # 6. Clear full-model gradients for the next step
        for param in self.model.parameters():
            param.grad = None
