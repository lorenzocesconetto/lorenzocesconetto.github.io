## Project Overview

This is a technical blog built with **Quarto**, focusing on deep-dive articles about Machine Learning, AI, and distributed GPU computing. Posts are written in Quarto Markdown (.qmd) with embedded Python code blocks that execute during build.

## Build Commands

```bash
# Preview site locally with hot reload
quarto preview

# Build the full site (outputs to _site/)
quarto render

# Render a single post
quarto render posts/2025-09-16-RoPE/index.qmd
```

## Python Environment

- Requires Python 3.13+
- Package manager: `uv`
- Install dependencies: `uv sync`

Key dependencies: PyTorch, Jupyter, Plotly, Matplotlib, NumPy, Seaborn

## Project Structure

- `posts/` - Blog articles in date-prefixed folders (e.g., `posts/2025-09-16-RoPE/`)
- `_quarto.yml` - Main Quarto configuration (navbar, themes, footer)
- `posts/_metadata.yml` - Default settings for all posts (freeze, caching)
- `_site/` - Generated static site (build output, git-ignored)
- `_freeze/` - Cached code execution outputs

## Writing Posts

Each post lives in its own folder under `posts/` with an `index.qmd` file. The folder name format is `YYYY-MM-DD-slug/`.

Posts use `freeze: auto` - code only re-executes when source changes. Use `cache: true` for expensive computations.

## Content Style

The blog targets a natural, idiomatic American English tone that's not overly formal. Posts should provide a smooth reading experience and be succinct while explaining complex technical concepts in depth.
