import json
from pathlib import Path


HISTORY_FILE = Path("quiz_history.json")


def load_history():
    if not HISTORY_FILE.exists():
        return []

    try:
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: Quiz history could not be read.")
        return []


def save_result(result):
    history = load_history()
    history.append(result)

    with HISTORY_FILE.open("w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)