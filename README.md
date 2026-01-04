# uvlab 

English | [日本語](./README_ja.md)


A minimalist JupyterLab template powered by `uv`.
Stop wasting time on environment setup and focus on writing your code.

## Features

* **Total Isolation**: `uv` instantly builds an independent virtual environment for each lab (`lab_*.py`).
* **Config Portability**: Fully self-contained configuration with `notebooks/` as the root directory.
* **Intelligent Launcher**: Automatically parses DocStrings to provide a menu-driven CLI.
* **Clean Operation**: Optimized for browser-based usage with reliable port release on `Ctrl+C`.

## Getting Started

### 1. Requirements

Ensure [uv](https://github.com/astral-sh/uv) is installed.

### 2. Launch

Run the launcher at the repository root:

```bash
python uvlab.py

```

### 3. Add a New Lab

Copy `lab/lab_sample.py` to a new file (e.g., `lab_ai.py`) and simply update the `dependencies` list at the top.

## Directory Structure

* `uvlab.py`: CLI launcher to start your labs.
* `lab/`: Contains lab definitions and Jupyter configurations.
* `notebooks/`: Workspace for all your `.ipynb` files.

## Important Notes

* **Browser Recommended**: VSCode's "Remote Jupyter Server" mode can be unstable with process management. Using a standard browser (`http://localhost:{port}/lab`) is highly recommended for the best experience.
