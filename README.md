# uvlab

English | [日本語](./README_ja.md)

A minimalist JupyterLab template for data scientists, leveraging the full power of `uv`.

Stop wasting time on environment setup and start focusing on your analysis.

## Features

* **One-File, One-Environment**: Each `lab/*.py` script contains both its own "dependencies" (inline metadata) and "Jupyter configurations." A single file is all you need.
* **Many-to-Many Flexibility**: Launch one environment (lab) for multiple competitions (notebooks), or use different environments for the same competition.
* **Zero-Config Portability**: Uses `pathlib` for dynamic path resolution. It works instantly no matter where you clone the repository.
* **Clean Operations**: Powered by `uv run` for automatic environment isolation and `Ctrl+C` for reliable process termination.

## Usage

### 1. Prerequisites

Ensure you have [uv](https://github.com/astral-sh/uv) installed.

### 2. Launch

Execute any script within the `lab/` directory directly.

```bash
# Launch with the default directory (root of notebooks/)
uv run lab/standard.py

# Launch for a specific competition/project folder
uv run lab/standard.py titanic

```

### 3. Command Line Options

You can override settings dynamically via arguments.

```bash
# Change the port number
uv run lab/standard.py --port 9000

# Launch without automatically opening a browser
uv run lab/standard.py --no-browser

```

## Adding a New Lab Environment

1. Copy `lab/sample.py` to a new file (e.g., `lab/pytorch.py`).
2. Edit the `dependencies` section at the top of the file to include your required libraries.
3. (Optional) Update `launch(default_competition="...")` in the `if __name__ == "__main__":` block to set a default target.

## Directory Structure

```text
.
├── lab/          # Environment definition scripts (entry points)
└── notebooks/    # Workspace for all .ipynb files (subfolders created automatically)

```

## Notes

* **Browser Recommended**: We strongly recommend using JupyterLab in a standard browser (`http://localhost:8888/lab`) rather than the VSCode Jupyter extension. This ensures full functionality and stable process management.
