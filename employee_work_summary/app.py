import json
import logging
import requests
from pathlib import Path
from datetime import datetime


# ---------------- LOGGING CONFIG ----------------
logging.basicConfig(
    filename="order_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ---------------- CUSTOM EXCEPTION ----------------
class InvalidOrderError(Exception):
    pass


# ---------------- BASE CLASS ----------------
class Order:
    def __init__(self, order_id, customer_name, unit_price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.unit_price = unit_price

    def calculate_total(self, quantity):
        return self.unit_price * quantity

    def __str__(self):
        return f"{self.customer_name} placed the order"


# ---------------- DERIVED CLASSES ----------------
class RegularOrder(Order):
    def calculate_total(self, quantity):
        return super().calculate_total(quantity)


class PremiumOrder(Order):
    def calculate_total(self, quantity):
        total = super().calculate_total(quantity)
        return total * 0.9   # 10% discount
    

def save_summary(record):
    OUTPUT_FILE = Path("product_summary.json")

    if OUTPUT_FILE.exists():
        data = json.loads(OUTPUT_FILE.read_text())
    else:
        data = []

    data.append(record)
    OUTPUT_FILE.write_text(json.dumps(data, indent=2))


# ---------------- PRODUCT VALIDATION ----------------
def validate_product(product_id):
    try:
        response = requests.get(
            f"https://fakestoreapi.com/products/{product_id}",
            timeout=5
        )
        response.raise_for_status()
        return True
    except Exception as e:
        logging.error(f"Product validation failed: {e}")
        return False


# ---------------- MAIN PROCESS ----------------
def product_summary():
    try:
        input_file = Path("order_log.json")
        output_file = Path("product_summary.json")

        if not input_file.exists():
            raise FileNotFoundError("Input file not found")

        with input_file.open("r") as file:
            orders = json.load(file)

        orders1 = json.loads(input_file.read_text())

        print(f"======{orders}")
        print(f"========{orders1}")

        summary_list = []

        for order in orders:
            if not validate_product(order["product_id"]):
                raise InvalidOrderError("Invalid product ID")

            if order["order_type"] == "premium":
                order_obj = PremiumOrder(
                    order["order_id"],
                    order["customer_name"],
                    order["unit_price"]
                )
            else:
                order_obj = RegularOrder(
                    order["order_id"],
                    order["customer_name"],
                    order["unit_price"]
                )

            total_amount = order_obj.calculate_total(order["quantity"])

            summary = {
                "order_id": order["order_id"],
                "customer_name": order["customer_name"],
                "order_type": order["order_type"],
                "total_amount": total_amount,
                "status": "Success",
                "processed_at": datetime.now().strftime("%d-%m-%Y %H:%M")
            }

            summary_list.append(summary)

        # with output_file.open("w") as file:
        #     json.dump(summary_list, file, indent=4)

        save_summary(summary)


        logging.info("Order summary created successfully")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("Error:", e)


# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    product_summary()
