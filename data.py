
import json
from models import Employee, Incident


def load_employees():
    loaded_employees = []

    try:
        with open("employees.json", "r") as file:
            employee_data = json.load(file)

            for item in employee_data:
                employee = Employee(item["name"], item["role"])
                employee.shifts = item.get("shifts", [])
                loaded_employees.append(employee)

    except FileNotFoundError:
        pass

    return loaded_employees


def save_employees(employees):
    employee_data = []

    for employee in employees:
        employee_data.append({
            "name": employee.name,
            "role": employee.role,
            "shifts": employee.shifts
        })

    with open("employees.json", "w") as file:
        json.dump(employee_data, file, indent=4)


def load_incidents():
    loaded_incidents = []

    try:
        with open("incidents.json", "r") as file:
            incident_data = json.load(file)

            for item in incident_data:
                incident = Incident(
                    item["title"],
                    item["description"],
                    item["severity"]
                )

                incident.time = item["time"]
                loaded_incidents.append(incident)

    except FileNotFoundError:
        pass

    return loaded_incidents


def save_incidents(incidents):
    incident_data = []

    for incident in incidents:
        incident_data.append({
            "title": incident.title,
            "description": incident.description,
            "severity": incident.severity,
            "time": str(incident.time)
        })

    with open("incidents.json", "w") as file:
        json.dump(incident_data, file, indent=4)


employees = load_employees()
incidents = load_incidents()