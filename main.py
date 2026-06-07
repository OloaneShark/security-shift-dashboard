
from models import Employee, Incident

from data import employees, incidents

from reports import view_shift_report

from data import employees, incidents, save_employees, save_incidents

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
        print("8. Exit")

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
            break
        else:
            print("Invalid choice.")


main()

##