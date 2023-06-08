import json
from flask import Flask
from controllers.EmployeeController import EmployeeController
from controllers.DepartmentController import DepartmentController

app = Flask(__name__)

employee_controller = EmployeeController()
department_controller = DepartmentController()

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route('/peoplesuite/apis/employees/<int:id>/profile', methods=['GET'])
def get_employee(id):
    return employee_controller.get(id=id)

@app.route('/peoplesuite/apis/employees/<int:id>/profile', methods=['POST'])
def create_employee(id):
    return employee_controller.create(id=id)

@app.route('/peoplesuite/apis/employees/<int:id>/photo', methods=['GET'])
def get_employee_photo(id):
    return employee_controller.get(id=id)

@app.route('/peoplesuite/apis/employees/<int:id>/photo', methods=['POST'])
def create_employee_photo(id):
    return employee_controller.update(id=id)

@app.route('/peoplesuite/apis/departments', methods=['GET'])
def get_departments():
    return department_controller.get()

@app.route('/peoplesuite/apis/departments/<int:id>/employees', methods=['GET'])
def get_employees_by_department(id):
    return department_controller.get(id=id)

if __name__ == '__main__':
    app.run(host ='0.0.0.0')
