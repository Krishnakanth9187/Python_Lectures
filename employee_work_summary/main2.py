import json
import logging
from datetime import datetime
from pathlib import Path
import requests


# ---------------- LOGGING SETUP ----------------

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()


# ---------------- CUSTOM EXCEPTION ----------------

class InvalidWorkLogError(Exception):
    pass


# ---------------- OOP CLASSES ----------------

class Employee:
    def __init__(self, emp_id, name, hourly_rate):
        self.emp_id = emp_id
        self.name = name
        self._hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked):
        return hours_worked * self._hourly_rate

    def __str__(self):
        return f"{self.emp_id} - {self.name}"


class PermanentEmployee(Employee):
    def calculate_salary(self, hours_worked):
        try:
            base_salary = super().calculate_salary(hours_worked)
            return base_salary + (base_salary * 0.20)
        except Exception as e:
            logger.error(e)


# ---------------- HOLIDAY API ----------------

API_URL = "https://date.nager.at/api/v3/PublicHolidays/2025/AT"

def is_holiday(date_str):
    try:
        response = requests.get(API_URL, timeout=5)
        print(f"response is {response.json()}")
        response.raise_for_status()

        holidays = response.json()

        for holiday in holidays:
            if holiday["date"] == date_str:
                return True

        return False

    except requests.RequestException:
        logger.error("Holiday API failure")
        raise ConnectionError("Holiday API failed")


# ---------------- FILE PATHS ----------------

INPUT_FILE = Path("work_log.json")
OUTPUT_FILE = Path("work_summary.json")


# ---------------- CORE LOGIC ----------------

def calculate_hours(login, logout):
    time_format = "%H:%M"
    # print(f"{login}")
    start = datetime.strptime(login, time_format)
    print(f"{start}")
    end = datetime.strptime(logout, time_format)
    print(f"{end}")

    print(end - start)

    date_hrs = (end - start)
    hours = date_hrs.total_seconds() / 3600
    print(f"=================={hours}")
    return round(hours, 2)


def save_summary(record):
    if OUTPUT_FILE.exists():
        data = json.loads(OUTPUT_FILE.read_text())
    else:
        data = []

    data.append(record)
    OUTPUT_FILE.write_text(json.dumps(data, indent=2))


def process_work_logs():
    try:
        print(f"========================={INPUT_FILE.read_text()}")
        employees = json.loads(INPUT_FILE.read_text()) # converts string to dict
         
        for emp in employees:
            try:
                if "login_time" not in emp or "logout_time" not in emp:
                    raise InvalidWorkLogError("Missing time fields")

                hours_worked = calculate_hours(
                    emp["login_time"],
                    emp["logout_time"]
                )

                if emp["employee_type"] == "permanent":
                    employee = PermanentEmployee(
                        emp["emp_id"],
                        emp["name"],
                        emp["hourly_rate"]
                    )
                else:
                    employee = Employee(
                        emp["emp_id"],
                        emp["name"],
                        emp["hourly_rate"]
                    )


                if is_holiday(emp["date"]):
                    final_salary = 0
                    status = "Holiday - No Pay"
                else:
                    final_salary = employee.calculate_salary(hours_worked)
                    status = "Success"

                summary = {
                    "emp_id": emp["emp_id"],
                    "name": emp["name"],
                    "working_hours": hours_worked,
                    "final_salary": final_salary,
                    "status": status,
                    "processed_at": datetime.now().strftime("%d-%m-%Y %H:%M")
                }

                save_summary(summary)
                logger.info(f"Processed {emp['emp_id']}")

            except (InvalidWorkLogError, ConnectionError) as err:
                logger.error(f"{emp.get('emp_id')} failed: {err}")

    except Exception as e:
        logger.error(f"Application failed: {e}")


# ---------------- RUN ----------------

if __name__ == "__main__":
    process_work_logs()
