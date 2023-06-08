import boto3
from dynamodb_client import dynamodb_client
from dynamodb_config import DYNAMODB_EMPLOYEE_TABLE_NAME

class EmployeeDAO:
    def __init__(self):
        self.table_name = DYNAMODB_EMPLOYEE_TABLE_NAME

    def get_employee(self, employee_id):
        response = dynamodb_client.get_item(
            TableName=self.table_name,
            Key={'EmployeeID': {'S': employee_id}}
        )
        return response.get('Item')

    def create_employee(self, employee_data):
        response = dynamodb_client.put_item(
            TableName=self.table_name,
            Item=employee_data
        )
        return response
