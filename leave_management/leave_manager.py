from exceptions import InvalidLeaveRequestError

class LeaveManager:
    def __init__(self, employee_id, employee_name, total_leaves):
        if total_leaves <= 0:
            raise InvalidLeaveRequestError("Total leaves must be greater than 0")

        self.employee_id = employee_id
        self.employee_name = employee_name
        self.remaining_leaves = total_leaves

    def apply_leave(self, requested_leaves):
        if requested_leaves <= 0:
            raise InvalidLeaveRequestError("Requested leaves must be greater than 0")

        if requested_leaves > self.remaining_leaves:
            raise InvalidLeaveRequestError(
                "Requested leaves exceed available balance"
            )

        self.remaining_leaves -= requested_leaves
        return self.remaining_leaves
