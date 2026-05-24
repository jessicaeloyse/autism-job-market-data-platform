from pathlib import Path


DEFAULT_EXCLUDED_DIRS = {
    ".git",
}


def load_gitignore_entries(gitignore_path=".gitignore"):

    excluded = set()

    gitignore = Path(gitignore_path)

    if not gitignore.exists():
        return excluded

    lines = gitignore.read_text().splitlines()

    for line in lines:

        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Ignore comments
        if line.startswith("#"):
            continue

        # Ignore complex rules for now
        if "*" in line or "!" in line:
            continue

        # Remove trailing slash
        line = line.rstrip("/")

        excluded.add(line)

    return excluded


def generate_tree(
    path: Path,
    excluded_dirs: set,
    prefix: str = ""
):

    entries = sorted(
        [
            entry
            for entry in path.iterdir()
            if entry.name not in excluded_dirs
        ],
        key=lambda e: (not e.is_dir(), e.name.lower())
    )

    tree = []

    for index, entry in enumerate(entries):

        connector = (
            "└── "
            if index == len(entries) - 1
            else "├── "
        )

        tree.append(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():

            extension = (
                "    "
                if index == len(entries) - 1
                else "│   "
            )

            subtree = generate_tree(
                entry,
                excluded_dirs,
                prefix + extension
            )

            tree.extend(subtree)

    return tree


if __name__ == "__main__":

    project_root = Path.cwd()

    gitignore_entries = load_gitignore_entries()

    excluded_dirs = (
        DEFAULT_EXCLUDED_DIRS
        .union(gitignore_entries)
    )

    tree = generate_tree(
        project_root,
        excluded_dirs
    )

    print("\n".join(tree))