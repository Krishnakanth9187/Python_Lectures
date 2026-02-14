# ---------------- OOP DESIGN ----------------
class Employee:
    def __init__(self, emp_id: str, name: str, hourly_rate: float):
        self.emp_id = emp_id
        self.name = name
        self._hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked: float) -> float:
        return hours_worked * self._hourly_rate

    def __str__(self):
        return f"Employee({self.emp_id}, {self.name})"


class PermanentEmployee(Employee):
    def calculate_salary(self, hours_worked: float) -> float:
        base_salary = super().calculate_salary(hours_worked)
        return base_salary * 1.20  # 20% bonus