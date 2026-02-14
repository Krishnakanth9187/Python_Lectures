from flask import Flask, request, jsonify
from datetime import datetime
import logging

from leave_manager import LeaveManager
from exceptions import InvalidLeaveRequestError
from storage import save_transaction

app = Flask(__name__)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/api/leave/apply", methods=["POST"])
def apply_leave():
    try:
        data = request.get_json()

        # Validate missing fields
        required_fields = [
            "employee_id",
            "employee_name",
            "total_leaves",
            "requested_leaves"
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        manager = LeaveManager(
            data["employee_id"],
            data["employee_name"],
            data["total_leaves"]
        )

        remaining = manager.apply_leave(data["requested_leaves"])

        response = {
            "employee_id": data["employee_id"],
            "employee_name": data["employee_name"],
            "total_leaves": data["total_leaves"],
            "requested_leaves": data["requested_leaves"],
            "remaining_leaves": remaining,
            "status": "Approved",
            "processed_at": datetime.now().strftime("%d-%m-%Y %H:%M")
        }

        save_transaction(response)
        logging.info(f"Leave approved for {data['employee_id']}")

        return jsonify(response), 200

    except InvalidLeaveRequestError as e:
        logging.error(str(e))
        return jsonify({"error": str(e)}), 400

    except Exception:
        logging.error("Internal server error")
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
