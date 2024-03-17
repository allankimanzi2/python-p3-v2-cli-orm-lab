from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

# New function, implement as described
def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")

# New function, implement as described
def find_employee_by_id():
    id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id)
    if employee:
        print(employee)
    else:
        print(f"Employee {id} not found")

# New function, implement as described
def create_employee():
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = int(input("Enter the employee's department id: "))
        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error creating employee: {e}")

# New function, implement as described
def update_employee():
    id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id)
    if not employee:
        print(f"Employee {id} not found")
        return

    try:
        new_name = input("Enter the employee's new name: ")
        new_job_title = input("Enter the employee's new job title: ")
        new_department_id = int(input("Enter the employee's new department id: "))
        employee.name = new_name
        employee.job_title = new_job_title
        employee.department_id = new_department_id
        employee.update()
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error updating employee: {e}")

# New function, implement as described
def delete_employee():
    id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id)
    if not employee:
        print(f"Employee {id} not found")
        return
    
    employee.delete()
    print(f"Employee {id} deleted")