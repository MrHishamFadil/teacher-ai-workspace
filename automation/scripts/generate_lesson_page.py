"""Preview future lesson page generation.

This beginner-safe script reads lessons-data.json and prints a plan.
It does not call AI services, send emails, collect student data, or edit files.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "lessons-data.json"


def main() -> None:
    lessons = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    print("Smart Path Study Hub: lesson generation preview")
    print("No files will be created by this placeholder script.")
    print()

    for lesson in lessons:
        print(
            f"Would prepare Grade {lesson['grade']} Unit {lesson['unit']} "
            f"Lesson {lesson['lessonNumber']}: {lesson['title']}"
        )
        print(f"Target page: {lesson['pagePath']}")
        print(f"Status: {lesson['status']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
