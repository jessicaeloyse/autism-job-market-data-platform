from pathlib import Path

from tree_generator import (
    generate_tree,
    load_gitignore_entries,
    DEFAULT_EXCLUDED_DIRS,
)


START_MARKER = "<!-- PROJECT_STRUCTURE_START -->"
END_MARKER = "<!-- PROJECT_STRUCTURE_END -->"


def build_structure_section(project_root: Path):

    gitignore_entries = load_gitignore_entries()

    excluded_dirs = (
        DEFAULT_EXCLUDED_DIRS
        .union(gitignore_entries)
    )

    tree = generate_tree(
        project_root,
        excluded_dirs
    )

    project_name = project_root.name

    tree_content = "\n".join(tree)

    return (
        f"{START_MARKER}\n\n"
        f"```text\n"
        f"{project_name}\n"
        f"{tree_content}\n"
        f"```\n\n"
        f"{END_MARKER}"
    )


def update_readme():

    project_root = Path.cwd()

    readme_path = project_root / "README.md"

    readme_content = readme_path.read_text()

    structure_section = build_structure_section(
        project_root
    )

    start_index = readme_content.index(
        START_MARKER
    )

    end_index = (
        readme_content.index(END_MARKER)
        + len(END_MARKER)
    )

    updated_content = (
        readme_content[:start_index]
        + structure_section
        + readme_content[end_index:]
    )

    readme_path.write_text(updated_content)

    print("README updated successfully.")


if __name__ == "__main__":

    update_readme()