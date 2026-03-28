import os
import csv

print("\nWelcome to Employee Database\n")

class Employee:
    def __init__(self, staff_id, first_name, last_name, department, dob, email, phone, salary, address):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.dob = dob
        self.email = email
        self.phone = phone
        self.salary = salary
        self.address = address


def staff_list():
    staffs = []

    if os.path.exists("employees.csv"):
        with open("employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)

            for row in reader:
                if row:
                    emp = Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    staffs.append(emp)

    return staffs


def generate_id():
    staffs = staff_list()

    if not staffs:
        return 1001

    last_id = max(int(emp.staff_id) for emp in staffs)
    return last_id + 1


def save(emp):

    with open("employees.csv","a",newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            emp.staff_id,
            emp.first_name,
            emp.last_name,
            emp.department,
            emp.dob,
            emp.email,
            emp.phone,
            emp.salary,
            emp.address
        ])


def rewrite(staffs):

    with open("employees.csv","w",newline="") as file:
        writer = csv.writer(file)

        for emp in staffs:
            writer.writerow([
                emp.staff_id,
                emp.first_name,
                emp.last_name,
                emp.department,
                emp.dob,
                emp.email,
                emp.phone,
                emp.salary,
                emp.address
            ])


def add_employee():

    staff_id = generate_id()
    print("Employee ID:", staff_id)

    first_name = input("Enter first name: ").lower()
    last_name = input("Enter last name: ").lower()
    department = input("Enter department: ").lower()
    dob = input("Enter date of birth: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    salary = input("Enter salary: ")
    address = input("Enter address: ")

    emp = Employee(staff_id,first_name,last_name,department,dob,email,phone,salary,address)

    save(emp)

    print("Employee added.\n")


def view():

    staffs = staff_list()

    if not staffs:
        print("No employees found.\n")
        return

    for emp in staffs:
        print("ID:", emp.staff_id)
        print("Name:", emp.first_name, emp.last_name)
        print("Department:", emp.department)
        print("DOB:", emp.dob)
        print("Email:", emp.email)
        print("Phone:", emp.phone)
        print("Salary:", emp.salary)
        print("Address:", emp.address)
        print()


def search():

    look = input("Enter employee ID or name: ").lower()

    staffs = staff_list()

    found = False

    for emp in staffs:
        if look == emp.staff_id or look in emp.first_name or look in emp.last_name:
            print(emp.staff_id, emp.first_name, emp.last_name, emp.department, emp.salary)
            found = True

    if not found:
        print("Employee not found.\n")


def update():

    look = input("Enter employee ID: ")

    staffs = staff_list()

    for emp in staffs:

        if look == emp.staff_id:

            print("Leave blank to keep old value\n")

            emp.first_name = input("New first name: ") or emp.first_name
            emp.last_name = input("New last name: ") or emp.last_name
            emp.department = input("New department: ") or emp.department
            emp.email = input("New email: ") or emp.email
            emp.phone = input("New phone: ") or emp.phone
            emp.salary = input("New salary: ") or emp.salary
            emp.address = input("New address: ") or emp.address

            rewrite(staffs)

            print("Employee updated.\n")
            return

    print("Employee ID not found.\n")


def delete():

    look = input("Enter employee ID to delete: ")

    staffs = staff_list()

    for emp in staffs:

        if look == emp.staff_id:

            staffs.remove(emp)

            rewrite(staffs)

            print("Employee deleted.\n")

            return

    print("Employee ID not found.\n")


while True:

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit\n")

    choice = input("Choose option: ")
    

    if choice == "1":
        add_employee()

    elif choice == "2":
        view()

    elif choice == "3":
        search()

    elif choice == "4":
        update()

    elif choice == "5":
        delete()

    elif choice == "6":
        print("Thank you for using Employee Database.")
        break
    else:
        print("Please choose from 1-6.")
