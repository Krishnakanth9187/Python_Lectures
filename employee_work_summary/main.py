import json
import logging
from datetime import datetime
from pathlib import Path
from employee import Employee, PermanentEmployee
import utils
import api








class InvalidWorkLogError(Exception):
    pass





# ---------------- MAIN PROCESS ----------------
def process_work_logs(input_file: Path, output_file: Path):
    try:
        with input_file.open("r") as f:
            logs = json.load(f)

        for log in logs:
            try:
                emp_id = log["emp_id"]
                name = log["name"]
                emp_type = log["employee_type"]
                rate = log["hourly_rate"]
                login = log["login_time"]
                logout = log["logout_time"]
                date = log["date"]

                # Employee Object
                if emp_type == "permanent":
                    employee = PermanentEmployee(emp_id, name, rate)
                else:
                    employee = Employee(emp_id, name, rate)

                # Holiday Check
                if api.is_public_holiday(date):
                    final_salary = 0
                    working_hours = 0
                    status = "Holiday"
                else:
                    working_hours = utils.calculate_working_hours(login, logout)
                    final_salary = employee.calculate_salary(working_hours)
                    status = "Success"

                summary = {
                    "emp_id": emp_id,
                    "name": name,
                    "working_hours": working_hours,
                    "final_salary": round(final_salary, 2),
                    "status": status,
                    "processed_at": datetime.now().strftime("%d-%m-%Y %H:%M")
                }

                utils.append_json_safe(output_file, summary)
                logging.info(f"Processed {emp_id} successfully")

            except KeyError as e:
                logging.error(f"Missing field: {e}")
                raise InvalidWorkLogError("Invalid work log structure")

    except Exception as e:
        logging.error(f"Processing failed: {e}")
        raise


# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    input_path = Path("work_log.json")
    output_path = Path("output_summary.json")

    process_work_logs(input_path, output_path)
