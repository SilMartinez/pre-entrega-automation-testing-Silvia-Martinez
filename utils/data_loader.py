import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_csv_login_data(filename: str):

    file_path = BASE_DIR / "data" / filename
    rows = []
    with file_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                (
                    row["username"],
                    row["password"],
                    row["should_pass"].strip().lower() == "true",
                )
            )
    return rows


def load_json(filename: str):
 
    file_path = BASE_DIR / "data" / filename
    with file_path.open(encoding="utf-8") as f:
        return json.load(f)