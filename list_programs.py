import os

def list_terminal_programs():
    paths = os.environ.get("PATH", "").split(":")
    programs = set()

    for path in paths:
        if os.path.isdir(path):
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                    programs.add(item)

    for prog in sorted(programs):
        print(prog)

if __name__ == "__main__":
    list_terminal_programs()

