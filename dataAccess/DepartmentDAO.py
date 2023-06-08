import boto3
from dynamodb_client import dynamodb_client

class DepartmentDAO:
    def __init__(self):
        self.table_name = "DYNAMODB_DEPARTMENT_TABLE_NAME"

    def get_department(self, department_id):
        response = dynamodb_client.get_item(
            TableName=self.table_name,
            Key={'DepartmentID': {'S': department_id}}
        )
        return response.get('Item')

    def create_department(self, department_data):
        response = dynamodb_client.put_item(
            TableName=self.table_name,
            Item=department_data
        )
        return response
