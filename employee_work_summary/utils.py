from datetime import datetime
import json
import logging
from pathlib import Path





def calculate_working_hours(login: str, logout: str) -> float:
    fmt = "%H:%M"
    login_time = datetime.strptime(login, fmt)
    logout_time = datetime.strptime(logout, fmt)
    delta = logout_time - login_time
    return round(delta.total_seconds() / 3600, 2)


def append_json_safe(path: Path, record: dict):
    try:
        if path.exists():
            with path.open("r") as f:
                data = json.load(f)
        else:
            data = []

        data.append(record)

        with path.open("w") as f:
            json.dump(data, f, indent=2)

    except Exception as e:
        logging.error(f"File write error: {e}")
        raise
