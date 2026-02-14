import json
import os

FILE_NAME = "leave_transactions.json"

def save_transaction(transaction):
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)

    with open(FILE_NAME, "r") as f:
        data = json.load(f)

    data.append(transaction)

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)
