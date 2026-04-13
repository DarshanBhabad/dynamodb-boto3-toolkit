#Creates DynamoDB table with composite key + GSI.
from .config import get_dynamodb_resource

def create_table():
    dynamodb = get_dynamodb_resource()

    table = dynamodb.create_table(
        TableName='StudentCourses',
        KeySchema=[
            {'AttributeName': 'student_id', 'KeyType': 'HASH'},
            {'AttributeName': 'course_id', 'KeyType': 'RANGE'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'student_id', 'AttributeType': 'S'},
            {'AttributeName': 'course_id', 'AttributeType': 'S'},
            {'AttributeName': 'status', 'AttributeType': 'S'}
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'StatusIndex',
                'KeySchema': [
                    {'AttributeName': 'status', 'KeyType': 'HASH'}
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    table.wait_until_exists()
    print("Table created successfully")