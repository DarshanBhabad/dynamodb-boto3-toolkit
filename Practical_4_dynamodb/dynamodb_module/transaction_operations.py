from .config import get_dynamodb_client

client = get_dynamodb_client()

def transactional_insert():

    client.transact_write_items(
        TransactItems=[
            {
                'Put': {
                    'TableName': 'StudentCourses',
                    'Item': {
                        'student_id': {'S': 'S500'},
                        'course_id': {'S': 'C900'},
                        'name': {'S': 'TransactionUser'},
                        'status': {'S': 'active'}
                    }
                }
            }
        ]
    )

    print("Transaction completed")