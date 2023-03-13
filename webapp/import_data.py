import json
from pathlib import Path

WEBAPP_DIR = Path(__file__).parent
BASE_DIR = WEBAPP_DIR.parent
DATA_DIR = BASE_DIR / "data"
LATEST_FILE = DATA_DIR / "latest.json"
REPORTS_DIR = DATA_DIR / "reports"


def combine_reports():
    reports = []
    for reports_file in REPORTS_DIR.glob("*.json"):
        with reports_file.open("r") as f:
            reports.append(json.load(f))

    return reports


def main():
    reports = combine_reports()
    frontend_data = {
        "reports": reports,
        "latest": json.loads(LATEST_FILE.read_text()),
    }
    combined_file = WEBAPP_DIR / "src" / "data" / "reports.json"
    combined_file.write_text(json.dumps(frontend_data, indent=2))


if __name__ == "__main__":
    main()
