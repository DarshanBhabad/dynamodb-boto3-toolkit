from .config import get_dynamodb_resource

dynamodb = get_dynamodb_resource()
table = dynamodb.Table('StudentCourses')


def batch_insert(items):

    with table.batch_writer() as batch:

        for item in items:
            batch.put_item(Item=item)

    print("Batch insert completed")