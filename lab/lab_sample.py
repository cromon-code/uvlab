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
import os
from jupyterlab.labapp import LabApp


def launch():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, "jupyter_lab_config.py")
    sys.argv = [sys.argv[0], f"--config={config_file}"]
    LabApp.launch_instance()

if __name__ == "__main__":
    launch()