import os
import json

def is_first_run(base_dir: str) -> bool:
    """
    Returns True if this is the first time the app is running
    on this machine.
    """
    os.makedirs(base_dir, exist_ok=True)
    first_run_file = os.path.join(base_dir, "first_run.json")

    if not os.path.exists(first_run_file):
        with open(first_run_file, "w") as f:
            json.dump({"first_run": False}, f)
        return True

    return False
