
from models import Employee, Incident

from reports import view_shift_report

from datetime import datetime

from data import (
    employees,
    incidents,
    schedules,
    time_logs,
    save_employees,
    save_incidents,
    save_schedules,
    save_time_logs
    )

    

def clock_in_employee():
    employee_id = input("Enter your employee ID: ").strip()

    for employee in employees:
        if employee.employee_id == employee_id:
            log = {
                "employee_id": employee.employee_id,
                "name": employee.name,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "clock_in": datetime.now().strftime("%H:%M"),
                "clock_out": None
            }

            time_logs.append(log)
            save_time_logs(time_logs)

            print(f"{employee.name} clocked in.")
            return

    print("Employee not found.")
    
    
def clock_out_employee():
    employee_id = input("Enter your employee ID: ").strip()

    for log in reversed(time_logs):
        if log["employee_id"] == employee_id and log["clock_out"] is None:
            log["clock_out"] = datetime.now().strftime("%H:%M")
            save_time_logs(time_logs)
            print(f"{log['name']} clocked out.")
            return

    print("No active clock-in found.")


def log_incident():
    title = input("Incident title: ").strip()
    description = input("Description: ").strip()
    severity = input("Severity: low / medium / high: ").strip()

    incident = Incident(title, description, severity)
    incidents.append(incident)

    save_incidents(incidents)

    print("Incident logged.")

    
def view_schedules():
    if not schedules:
        print("No schedules found.")
        return

    for schedule in schedules:
        print(f"\nEmployee: {schedule['name']}")
        print(f"Date: {schedule['date']}")
        print(f"Time: {schedule['start_time']} - {schedule['end_time']}")
        print(f"Post: {schedule['post']}")
          

def main():
    while True:
        print("\nSecurity Shift Dashboard")
        print("1. Clock in employee")
        print("2. Clock out employee")
        print("3. Log incident")
        print("4. View schedules")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            clock_in_employee()
        elif choice == "2":
            clock_out_employee()
        elif choice == "3":
            log_incident()
        elif choice == "4":
            view_schedules()
        elif choice == "5":
            break


main()
