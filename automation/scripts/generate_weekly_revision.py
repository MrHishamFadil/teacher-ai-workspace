"""Preview future weekly revision generation.

This beginner-safe script reads lessons-data.json and groups lesson metadata.
It does not call AI services, send emails, collect student data, or edit files.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = ROOT / "lessons-data.json"


def main() -> None:
    lessons = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    groups: dict[tuple[int, int], list[dict]] = defaultdict(list)

    for lesson in lessons:
        groups[(lesson["grade"], lesson["unit"])].append(lesson)

    print("Smart Path Study Hub: weekly revision generation preview")
    print("No files will be created by this placeholder script.")
    print()

    for (grade, unit), unit_lessons in sorted(groups.items()):
        print(f"Would prepare a revision draft for Grade {grade}, Unit {unit}")
        for lesson in unit_lessons:
            print(f"- Lesson {lesson['lessonNumber']}: {lesson['title']}")
        print("-" * 60)


if __name__ == "__main__":
    main()
