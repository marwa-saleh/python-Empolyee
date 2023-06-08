class Department:
    def __init__(self, department_id, cost_center, parent_department_id=None):
        self.department_id = department_id
        self.cost_center = cost_center
        self.parent_department_id = parent_department_id
