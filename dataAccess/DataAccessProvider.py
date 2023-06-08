from dataAccess.EmployeeDAO import EmployeeDAO
from dataAccess.DepartmentDAO import DepartmentDAO

class DataAccessProvider:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataAccessProvider, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.employee_dao = EmployeeDAO()
        self.department_dao = DepartmentDAO()

    def get_employee(self, employee_id):
        return self.employee_dao.get_employee(employee_id)

    def create_employee(self, employee_data):
        return self.employee_dao.create_employee(employee_data)

    def get_department(self, department_id):
        return self.department_dao.get_department(department_id)

    def create_department(self, department_data):
        return self.department_dao.create_department(department_data)

