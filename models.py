from datetime import datetime


from datetime import datetime


class Employee:
    def __init__(self, name, role, employee_id=None):
        self.name = name
        self.role = role
        self.employee_id = employee_id
        self.shifts = []

    def clock_in(self):
        if self.shifts and self.shifts[-1]["clock_out"] is None:
            print("Employee is already clocked in.")
            return False

        self.shifts.append({
            "clock_in": str(datetime.now()),
            "clock_out": None
        })
        return True

    def clock_out(self):
        if not self.shifts:
            print("Warning: No clock in detected.")
            return False

        if self.shifts[-1]["clock_out"] is not None:
            print("Warning: No active clock in detected.")
            return False

        self.shifts[-1]["clock_out"] = str(datetime.now())
        return True

    def __str__(self):
        shift_info = ""

        for index, shift in enumerate(self.shifts, start=1):
            shift_info += (
                f"\n  Shift {index}: "
                f"Clock in: {shift['clock_in']} | "
                f"Clock out: {shift['clock_out']}"
            )

        return f"{self.name} - {self.role}{shift_info}"
    
    
class Incident:
    def __init__(self, title, description, severity):
        self.title = title
        self.description = description
        self.severity = severity
        self.time = datetime.now()

    def __str__(self):
        return f"[{self.severity}] {self.title} at {self.time}: {self.description}"
    