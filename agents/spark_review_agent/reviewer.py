from pathlib import Path

from rules import RULES


def review_file(file_path):
    findings = []

    lines = Path(file_path).read_text().splitlines()

    for line_number, line in enumerate(lines, start=1):

        for rule in RULES:

            if rule["pattern"] in line:

                findings.append(
                    {
                        "rule": rule["name"],
                        "line": line_number,
                        "code": line.strip(),
                        "message": rule["message"],
                    }
                )

    return findings


if __name__ == "__main__":

    findings = review_file(
        "sample_code/bad_spark_code.py"
    )

    if findings:

        print("\n=== Findings ===\n")

        for finding in findings:

            print(f"[{finding['rule']}]")
            print(f"Line {finding['line']}: {finding['code']}")
            print(f"{finding['message']}\n")

    else:

        print("No issues found.")