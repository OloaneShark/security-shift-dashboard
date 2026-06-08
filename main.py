
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

def add_employee():
    name = input("Employee name: ").strip()
    role = input("Role: ").strip()

    for employee in employees:
        if employee.name.lower() == name.lower() and employee.role.lower() == role.lower():
            print("Duplicate employee detected under the same role.")
            return

    employee = Employee(name, role)
    employees.append(employee)

    save_employees(employees)
    
    print("Employee added.")
    
    
def remove_employee():
    name = input("Employee name to remove: ").strip()
    role = input("Employee role: ").strip()

    for employee in employees:
        if employee.name.lower() == name.lower() and employee.role.lower() == role.lower():
            employees.remove(employee)
            save_employees(employees)
            print("Employee removed.")
            return

    print("Employee not found.")


def clock_in_employee():
    name = input("Who is clocking in? ").strip()

    for employee in employees:
        if employee.name.lower() == name.lower():
            if employee.clock_in():
                save_employees(employees)
                print(f"{employee.name} clocked in.")
            return

    print("Employee not found.")
    
    
def clock_out_employee():
    name = input("Who is clocking out? ").strip()

    for employee in employees:
        if employee.name.lower() == name.lower():
            if employee.clock_out():
                save_employees(employees)
                print(f"{employee.name} clocked out.")
            return

    print("Employee not found.")


def log_incident():
    title = input("Incident title: ").strip()
    description = input("Description: ").strip()
    severity = input("Severity: low / medium / high: ").strip()

    incident = Incident(title, description, severity)
    incidents.append(incident)

    save_incidents(incidents)

    print("Incident logged.")
    
    
def remove_incident():
    title = input("Incident title to remove: ").strip()

    for incident in incidents:
        if incident.title.lower() == title.lower():
            incidents.remove(incident)
            save_incidents(incidents)
            print("Incident removed.")
            return

    print("Incident not found.")


def view_shift_report():
    print("\n--- Employees ---")
    for employee in employees:
        print(employee)

    print("\n--- Incidents ---")
    for incident in incidents:
        print(incident)


def add_schedule():
    name = input("Employee name: ").strip()
    date = input("Date: ").strip()
    start_time = input("Start time: ").strip()
    end_time = input("End time: ").strip()
    post = input("Post/location: ").strip()

    schedule = {
        "name": name,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "post": post
    }

    schedules.append(schedule)
    save_schedules(schedules)

    print("Schedule added.")
    
    
def view_schedules():
    if not schedules:
        print("No schedules found.")
        return

    for schedule in schedules:
        print(f"\nEmployee: {schedule['name']}")
        print(f"Date: {schedule['date']}")
        print(f"Time: {schedule['start_time']} - {schedule['end_time']}")
        print(f"Post: {schedule['post']}")
        
        
def clock_in_time_log():
    name = input("Who is clocking in? ").strip()

    log = {
        "name": name,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "clock_in": datetime.now().strftime("%H:%M"),
        "clock_out": None
    }

    time_logs.append(log)
    save_time_logs(time_logs)

    print(f"{name} clocked in.")
    
    
def clock_out_time_log():
    name = input("Who is clocking out? ").strip()

    for log in reversed(time_logs):
        if log["name"].lower() == name.lower() and log["clock_out"] is None:
            log["clock_out"] = datetime.now().strftime("%H:%M")
            save_time_logs(time_logs)
            print(f"{name} clocked out.")
            return

    print("No active clock-in found.")
    
    



def main():
    while True:
        print("\nSecurity Shift Dashboard")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Clock in employee")
        print("4. Clock out employee")
        print("5. Log incident")
        print("6. Remove incident")
        print("7. View shift report")
        print("8. Add schedule")
        print("9. View schedules")
        print("10. Clock in time log")
        print("11. Clock out time log")
        print("12. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            clock_in_employee()
        elif choice == "4":
            clock_out_employee()
        elif choice == "5":
            log_incident()
        elif choice == "6":
            remove_incident()
        elif choice == "7":
            view_shift_report()
        elif choice == "8":
            add_schedule()
        elif choice == "9":
            view_schedules()
        elif choice == "10":
            clock_in_time_log()
        elif choice == "11":
            clock_out_time_log()
        elif choice == "12":
            break


main()
