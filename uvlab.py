import subprocess
import os
import sys
import ast

def get_lab_info():
    """Get the name and DocString from lab_*.py in the lab/ directory"""
    lab_dir = "lab"
    if not os.path.exists(lab_dir):
        return []
    
    files = sorted([f for f in os.listdir(lab_dir) if f.startswith("lab_") and f.endswith(".py")])
    labs = []

    for f in files:
        path = os.path.join(lab_dir, f)
        name = f.replace("lab_", "").replace(".py", "")
        desc = "No description"
        
        try:
            with open(path, "r", encoding="utf-8") as file:
                tree = ast.parse(file.read())
                doc = ast.get_docstring(tree)
                if doc:
                    desc = doc.strip().split('\n')[0]
        except Exception:
            pass
            
        labs.append({"file": f, "name": name, "desc": desc})
    return labs

def main():
    labs = get_lab_info()
    if not labs:
        print("\nError: 'lab/' directory is empty or missing.")
        return

    no_w = 2
    name_w = 11
    
    print(f"\n{'No':>{no_w}} | {'Name':<{name_w}} | {'Description'}")
    print(f"{'-' * no_w}-|-{'-' * name_w}-|-{'-' * 20}")

    for i, lab in enumerate(labs, 1):
        print(f"{i:>{no_w}} | {lab['name']:<{name_w}} | {lab['desc']}")

    try:
        choice = input("\nSelect number or name (q to quit): ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("")
        sys.exit(0)

    if choice == 'q':
        return

    target_file = None
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(labs):
            target_file = labs[idx]['file']
    else:
        for lab in labs:
            if lab['name'] == choice:
                target_file = lab['file']
                break

    if target_file:
        print(f"\n[ NOTE ]")
        print(r"  - Use Browser: http://localhost:{port}/lab")
        print(f"  - VSCode's 'Remote Server' mode is NOT recommended (may be unstable).")
        print(f"  - Press Ctrl+C to stop the server.\n")
        script_path = os.path.join("lab", target_file)
        proc = subprocess.Popen(["uv", "run", script_path])

        try:
            proc.wait()
        except KeyboardInterrupt:
            proc.wait()
            print("\nShutting down Jupyer Lab...")
            proc.terminate()

            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()

            sys.exit(0)

        except subprocess.CalledProcessError:
            print(f"\n [Error] Failed to run {target_file}")
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()