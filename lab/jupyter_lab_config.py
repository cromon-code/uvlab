import os


c = get_config()  # type: ignore

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
notebooks_dir = os.path.join(repo_root, "notebooks")
print(f"--- Jupyter Root: {notebooks_dir} ---")

c.ServerApp.root_dir = notebooks_dir

c.ServerApp.open_browser = True
c.ServerApp.port = 8888
c.ServerApp.ip = "localhost"

c.ServerApp.quit_button = True
c.ServerApp.answer_yes = True

# If you want the server to stop automatically 
# when you close the browser tab, use the following (optional)
# c.ServerApp.shutdown_no_activity_timeout = 30