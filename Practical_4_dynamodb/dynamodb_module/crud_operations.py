from .config import get_dynamodb_resource
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from .error_handler import handle_error

dynamodb = get_dynamodb_resource()
table = dynamodb.Table('StudentCourses')


def insert_item(item):
    try:
        table.put_item(Item=item)
        print("Item inserted")

    except ClientError as e:
        handle_error(e)


def query_by_student(student_id):

    response = table.query(
        KeyConditionExpression=Key('student_id').eq(student_id)
    )

    for item in response['Items']:
        print(item)


def query_by_status(status):

    response = table.query(
        IndexName='StatusIndex',
        KeyConditionExpression=Key('status').eq(status)
    )

    for item in response['Items']:
        print(item)


def update_marks(student_id, course_id, new_marks):

    try:
        table.update_item(
            Key={
                'student_id': student_id,
                'course_id': course_id
            },
            UpdateExpression="SET marks = :m",
            ConditionExpression="marks < :m",
            ExpressionAttributeValues={
                ':m': new_marks
            }
        )

        print("Marks updated")

    except ClientError as e:
        handle_error(e)

def delete_item(student_id, course_id):

    try:
        table.delete_item(
            Key={
                'student_id': student_id,
                'course_id': course_id
            }
        )

        print("Item deleted successfully")

    except ClientError as e:
        handle_error(e)


def scan_with_pagination():

    response = table.scan()

    while True:

        for item in response['Items']:
            print(item)

        if 'LastEvaluatedKey' not in response:
            break

        response = table.scan(
            ExclusiveStartKey=response['LastEvaluatedKey']
        )