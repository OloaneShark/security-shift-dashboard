
from dotenv import load_dotenv

import os

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


load_dotenv(".env")

MASTER_PASSWORD = os.getenv("MASTER_PASSWORD")


def check_admin_password():
    attempts = 3

    while attempts > 0:
        password = input("Enter admin password: ").strip()

        if password == MASTER_PASSWORD:
            print("Access granted.")
            return True

        attempts -= 1

        if attempts > 0:
            print(f"Incorrect password. {attempts} attempt(s) remaining.")
        else:
            print("Too many failed attempts. Access denied.")

    return False


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
    
    
def assign_employee_id():
    name = input("Employee name: ").strip()
    role = input("Employee role: ").strip()
    employee_id = input("Employee ID to assign: ").strip()

    for employee in employees:
        if employee.name.lower() == name.lower() and employee.role.lower() == role.lower():
            employee.employee_id = employee_id
            save_employees(employees)
            print(f"Employee ID {employee_id} assigned to {employee.name}.")
            return

    print("Employee not found.")


"""this was added to help me check all employees on the roster
without having to open up the employees.json file"""
def view_employee_roster():
    if not employees:
        print("No employees found.")
        return

    sorted_employees = sorted(
        employees,
        key=lambda employee: employee.name.split()[-1].lower()
    )

    print("\n--- Employee Roster ---")

    for employee in sorted_employees:
        print(f"[{employee.name}, {employee.role}, {employee.employee_id}]")

    
def add_schedule():
    employee_id = input("Employee ID: ").strip()
    date = input("Date: ").strip()
    start_time = input("Start time: ").strip()
    end_time = input("End time: ").strip()
    post = input("Post/location: ").strip()

    schedule = {
        "employee_id": employee_id,
        "date": date,
        "start_time": start_time,
        "end_time": end_time,
        "post": post
    }

    schedules.append(schedule)
    save_schedules(schedules)

    print("Schedule added.")
    
    
def remove_schedule():
    if not schedules:
        print("No schedules found.")
        return

    for index, schedule in enumerate(schedules, start=1):
        print(f"\n{index}. Employee ID: {schedule['employee_id']}")
        print(f"Date: {schedule['date']}")
        print(f"Time: {schedule['start_time']} - {schedule['end_time']}")
        print(f"Post: {schedule['post']}")

    try:
        choice = int(input("Which schedule number do you want to remove? "))

        if 1 <= choice <= len(schedules):
            removed_schedule = schedules.pop(choice - 1)
            save_schedules(schedules)
            print(f"Removed schedule for employee ID {removed_schedule['employee_id']}.")
        else:
            print("Invalid schedule number.")

    except ValueError:
        print("Please enter a valid number.")
        
  
def view_time_logs():
    if not time_logs:
        print("No time logs found.")
        return

    for index, log in enumerate(time_logs, start=1):
        print(f"\nTime Log #{index}")
        print(f"Employee ID: {log.get('employee_id', 'N/A')}")
        print(f"Name: {log.get('name', 'N/A')}")
        print(f"Date: {log.get('date', 'N/A')}")
        print(f"Clock In: {log.get('clock_in', 'N/A')}")
        print(f"Clock Out: {log.get('clock_out', 'N/A')}")
  
        
def remove_incident():
    if not incidents:
        print("No incidents found.")
        return

    for index, incident in enumerate(incidents, start=1):
        print(f"\n{index}. {incident.title}")
        print(f"Severity: {incident.severity}")
        print(f"Time: {incident.time}")

    try:
        choice = int(input("Which incident number do you want to remove? "))

        if 1 <= choice <= len(incidents):
            removed_incident = incidents.pop(choice - 1)
            save_incidents(incidents)
            print(f"Removed incident: {removed_incident.title}")
        else:
            print("Invalid incident number.")

    except ValueError:
        print("Please enter a valid number.")


def view_shift_report():
    print("\n--- Shift Report ---")

    print("\n--- Employees ---")
    if not employees:
        print("No employees found.")
    else:
        for employee in employees:
            print(f"\nName: {employee.name}")
            print(f"Role: {employee.role}")
            print(f"Employee ID: {getattr(employee, 'employee_id', 'N/A')}")

    print("\n--- Schedules ---")
    if not schedules:
        print("No schedules found.")
    else:
        for schedule in schedules:
            print(f"\nEmployee ID: {schedule.get('employee_id', 'N/A')}")
            print(f"Date: {schedule.get('date', 'N/A')}")
            print(f"Time: {schedule.get('start_time', 'N/A')} - {schedule.get('end_time', 'N/A')}")
            print(f"Post: {schedule.get('post', 'N/A')}")

    print("\n--- Time Logs ---")
    if not time_logs:
        print("No time logs found.")
    else:
        for log in time_logs:
            print(f"\nEmployee ID: {log.get('employee_id', 'N/A')}")
            print(f"Name: {log.get('name', 'N/A')}")
            print(f"Date: {log.get('date', 'N/A')}")
            print(f"Clock In: {log.get('clock_in', 'N/A')}")
            print(f"Clock Out: {log.get('clock_out', 'N/A')}")

    print("\n--- Incidents ---")
    if not incidents:
        print("No incidents found.")
    else:
        for incident in incidents:
            print(f"\nTitle: {incident.title}")
            print(f"Description: {incident.description}")
            print(f"Severity: {incident.severity}")
            print(f"Time: {incident.time}")
  

def employee_editor():
    while True:
        print("\nEmployee Editor")
        print("1. Add employee")
        print("2. Remove employee")
        print("3. Assign employee ID")
        print("4. View employee roster")
        print("5. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            assign_employee_id()
        elif choice == "4":
            view_employee_roster()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def schedule_editor():
    while True:
        print("\nSchedule Editor")
        print("1. Add schedule")
        print("2. Remove schedule")
        print("3. Back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_schedule()
        elif choice == "2":
            remove_schedule()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def admin_menu():
    while True:
        print("\nAdmin Dashboard")
        print("1. Employee Editor")
        print("2. Schedule Editor")
        print("3. View time logs")
        print("4. Remove incident")
        print("5. View shift report")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            employee_editor()
        elif choice == "2":
            schedule_editor()
        elif choice == "3":
            view_time_logs()
        elif choice == "4":
            remove_incident()
        elif choice == "5":
            view_shift_report()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
            
            
if check_admin_password():
    admin_menu()