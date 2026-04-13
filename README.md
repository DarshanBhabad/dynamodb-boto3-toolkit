DynamoDB Python Wrapper (Boto3)

A modular, production-ready Python package for AWS DynamoDB operations. This project demonstrates advanced database patterns including composite keys, Global Secondary Indexes (GSI), ACID transactions, and conditional updates using the boto3 SDK.

📌 Project Overview

The goal of this project is to provide a robust interface for managing a StudentCourses table. It moves beyond simple CRUD by implementing efficient pagination, batch processing, and error-handling mechanisms suitable for real-world cloud applications.

🛠 Tech Stack

Language: Python 3.x

SDK: Boto3 (AWS SDK for Python)

Database: Amazon DynamoDB

Cloud Provider: Amazon Web Services (AWS)

📂 Project Structure

Practical_4_dynamodb/
│
├── dynamodb_module/           # Core Package
│   ├── __init__.py            # Module initialization
│   ├── config.py              # AWS Client/Resource configuration
│   ├── table_manager.py       # Table creation & GSI setup
│   ├── crud_operations.py      # Item management (Query, Scan, Update)
│   ├── batch_operations.py     # High-throughput batch writes
│   ├── transaction_operations.py # ACID transaction logic
│   └── error_handler.py       # AWS exception handling logic
│
└── main.py                    # Execution entry point


📐 Database Design

Table: StudentCourses

Key Type

Attribute Name

Data Type

Partition Key (PK)

student_id

String (S)

Sort Key (SK)

course_id

String (S)

Global Secondary Index (GSI)

Index Name: StatusIndex

Partition Key: status (S)

Projection: ALL (Enables efficient querying of students by their enrollment status).

🚀 Key Features

1. Production-Lean Operations

Conditional Updates: The update_marks function ensures data integrity by only updating if the new marks are higher than the existing ones (ConditionExpression).

Pagination: Handles large dataset scanning using the LastEvaluatedKey token to prevent memory overflows.

Batch Processing: Utilizes batch_writer() to group multiple put operations, reducing the number of network calls.

2. ACID Transactions

Implements transact_write_items to ensure all-or-nothing operations, critical for maintaining consistency across complex data workflows.

3. Robust Error Handling

Centralized handle_error function manages common AWS exceptions:

ProvisionedThroughputExceededException (with retry logic).

ConditionalCheckFailedException.

⚙️ Setup & Usage

Configure AWS Credentials:
Ensure your AWS CLI is configured with aws configure.

Install Dependencies:

pip install boto3


Run the Application:

python main.py


👨‍💻 Author

Darshan Ganesh Bhabad 

Cloud Native Applications 
