class Employee:
    def __init__(self, employee_id, first_name, last_name, start_date, country, department_id, title, manager_id=None, manager_name=None, photo=None, profile_url=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = start_date
        self.country = country
        self.department_id = department_id
        self.title = title
        self.manager_id = manager_id
        self.manager_name = manager_name
        self.photo = photo
        self.profile_url = profile_url
