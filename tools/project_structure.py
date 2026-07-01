from pathlib import Path

EXCLUDED = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules",
    "dist",
    "build"
}

OUTPUT = "project_structure.md"


def write_tree(path: Path, file, prefix=""):
    entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    entries = [
        e for e in entries
        if e.name not in EXCLUDED
    ]

    for i, entry in enumerate(entries):

        connector = "└── " if i == len(entries)-1 else "├── "

        file.write(f"{prefix}{connector}{entry.name}\n")

        if entry.is_dir():
            extension = "    " if i == len(entries)-1 else "│   "
            write_tree(entry, file, prefix + extension)


if __name__ == "__main__":

    root = Path(".")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("# OPTISWIMM PROJECT STRUCTURE\n\n")
        write_tree(root, f)

    print(f"Structure enregistrée dans {OUTPUT}")