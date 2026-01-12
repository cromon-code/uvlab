# /// script
# dependencies = [
#   "jupyterlab", "pandas", "matplotlib"
# ]
# ///

"""
UV Lab Template
We recommend using a browser (external integration such as VSCode is not recommended).
"""

import sys
import argparse
from pathlib import Path
from jupyterlab.labapp import LabApp


PROJECT_ROOT = Path(__file__).resolve().parents[2]

def launch(default_competition: str = None):
    """generic function to launch Jupyter Lab in a custom env
    """
    parser = argparse.ArgumentParser(description="Launch JupyterLab")

    # specify root directory as the first argument
    parser.add_argument(
        "competition", type=str, nargs="?", default=default_competition,
        help="Competition or course name (optional)"
    )
    parser.add_argument("--port", type=int, default=8888, help="Port to use")
    parser.add_argument(
        "--no-browser", action="store_false", dest="open_browser", 
        help="Don't open browser"
    )
    args, unknown = parser.parse_known_args()

    # root directory decision logic
    notebooks_base = PROJECT_ROOT / "notebooks"

    if args.competition:
        root_dir = notebooks_base / args.competition
    else:
        root_dir = notebooks_base
    
    root_dir.mkdir(parents=True, exist_ok=True)

    sys.argv = [
        sys.argv[0],
        f"--ServerApp.root_dir={root_dir.as_posix()}",
        f"--ServerApp.port={args.port}",
        f"--ServerApp.open_browser={args.open_browser}",
        "--ServerApp.ip=localhost",
        "--ServerApp.quit_button=True",
        "--ServerApp.answer_yes=True",
    ] + unknown

    # user feedback
    target_label = args.competition if args.competition else "All Notebooks"
    print(f"Target: [{target_label}]")
    print(f"Path  : {root_dir}")

    LabApp.launch_instance()

if __name__ == "__main__":
    launch(default_competition=None)