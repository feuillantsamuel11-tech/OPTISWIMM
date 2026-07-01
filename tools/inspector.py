"""
OPTISWIMM Inspector V1
Project auditing tool

Author: OPTISWIMM
"""

from pathlib import Path
import ast
import json
from datetime import datetime


EXCLUDED_DIRS = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "node_modules",
    ".streamlit",
    ".idea",
    ".vscode",
    "dist",
    "build",
}


class ProjectInspector:

    def __init__(self, root_path):

        self.root = Path(root_path)

        self.stats = {
            "python_files": 0,
            "total_lines": 0,
            "classes": 0,
            "functions": 0,
            "todos": 0,
            "fixmes": 0,
            "empty_files": [],
            "large_files": [],
            "errors": [],
        }

    # --------------------------------------------------

    def scan(self):

        for file in self.root.rglob("*.py"):

            if any(part in EXCLUDED_DIRS for part in file.parts):
                continue

            self.inspect_file(file)

    # --------------------------------------------------

    def inspect_file(self, filepath):

        try:

            source = filepath.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            lines = source.splitlines()

            self.stats["python_files"] += 1
            self.stats["total_lines"] += len(lines)

            if len(lines) == 0:
                self.stats["empty_files"].append(str(filepath))

            if len(lines) > 500:
                self.stats["large_files"].append(
                    (str(filepath), len(lines))
                )

            self.stats["todos"] += source.count("TODO")
            self.stats["fixmes"] += source.count("FIXME")

            tree = ast.parse(source)

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):
                    self.stats["classes"] += 1

                elif isinstance(
                    node,
                    (
                        ast.FunctionDef,
                        ast.AsyncFunctionDef
                    )
                ):
                    self.stats["functions"] += 1

        except Exception as e:

            self.stats["errors"].append(
                f"{filepath}: {e}"
            )

    # --------------------------------------------------

    def markdown_report(self):

        report = []

        report.append("# OPTISWIMM PROJECT REPORT\n")

        report.append(
            f"Generated: {datetime.now()}\n"
        )

        report.append("---\n")

        report.append(f"Python files : {self.stats['python_files']}")
        report.append(f"Lines of code : {self.stats['total_lines']}")
        report.append(f"Classes : {self.stats['classes']}")
        report.append(f"Functions : {self.stats['functions']}")
        report.append(f"TODO : {self.stats['todos']}")
        report.append(f"FIXME : {self.stats['fixmes']}")

        report.append("\n## Large files\n")

        for file, size in self.stats["large_files"]:
            report.append(f"- {file} ({size} lines)")

        report.append("\n## Empty files\n")

        for file in self.stats["empty_files"]:
            report.append(f"- {file}")

        report.append("\n## Errors\n")

        for error in self.stats["errors"]:
            report.append(f"- {error}")

        return "\n".join(report)

    # --------------------------------------------------

    def save_reports(self):

        reports = self.root / "reports"

        reports.mkdir(exist_ok=True)

        md = reports / "project_report.md"
        js = reports / "project_report.json"

        md.write_text(
            self.markdown_report(),
            encoding="utf-8"
        )

        js.write_text(
            json.dumps(
                self.stats,
                indent=4,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )

    # --------------------------------------------------

    def run(self):

        print("=" * 50)
        print("OPTISWIMM INSPECTOR")
        print("=" * 50)

        self.scan()

        self.save_reports()

        print(f"Python files : {self.stats['python_files']}")
        print(f"Lines : {self.stats['total_lines']}")
        print(f"Classes : {self.stats['classes']}")
        print(f"Functions : {self.stats['functions']}")
        print()
        print("Report generated in reports/")


if __name__ == "__main__":

    inspector = ProjectInspector(".")
    inspector.run()