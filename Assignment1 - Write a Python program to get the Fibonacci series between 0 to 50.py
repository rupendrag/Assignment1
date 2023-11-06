import json

class Employee:
    def __init__(self, name, DOB, height, city, state):
        self.name = name
        self.DOB = DOB
        self.height = height
        self.city = city
        self.state = state

employee_data = [
    {
        "name": "John Doe",
        "DOB": "1990-05-15",
        "height": 175,
        "city": "New York",
        "state": "New York"
    },
    {
        "name": "Jane Smith",
        "DOB": "1988-03-20",
        "height": 163,
        "city": "Los Angeles",
        "state": "California"
    },
    {
        "name": "Michael Johnson",
        "DOB": "1995-09-10",
        "height": 180,
        "city": "Chicago",
        "state": "Illinois"
    },
    {
        "name": "Emily Davis",
        "DOB": "1992-07-05",
        "height": 168,
        "city": "Houston",
        "state": "Texas"
    },
    {
        "name": "David Wilson",
        "DOB": "1987-12-25",
        "height": 172,
        "city": "Miami",
        "state": "Florida"
    }
]

file_name = "Employee.json"

with open(file_name, 'w') as json_file:
    json.dump(employee_data, json_file, indent=4)

print(f"JSON data has been written to {file_name}")

with open(file_name, 'r') as file:
    employee_data = json.load(file)

employees = []
for emp_info in employee_data:
    employee = Employee(emp_info["name"], emp_info["DOB"], emp_info["height"], emp_info["city"], emp_info["state"])
    employees.append(employee)

for employee in employees:
    print(f"Name: {employee.name}, DOB: {employee.DOB}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")
