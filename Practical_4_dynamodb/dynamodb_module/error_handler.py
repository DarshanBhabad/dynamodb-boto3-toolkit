#for handling Aws exceptions
from botocore.exceptions import ClientError
import time

def handle_error(e):
    code = e.response['Error']['Code']

    if code == 'ProvisionedThroughputExceededException':
        print("Throughput exceeded. Retrying...")
        time.sleep(2)

    elif code == 'ConditionalCheckFailedException':
        print("Conditional check failed.")

    else:
        print("Unexpected error:", e)