# DynamoDB Boto3 Toolkit

A robust, production-lean Python module designed for high-performance DynamoDB operations. This project demonstrates best practices in schema design, indexing, and complex data operations using the `boto3` SDK.

## 🚀 Features

This package provides a wrapper around `boto3` to handle:
* [cite_start]**Advanced Key Design**: Implementation of Composite Primary Keys (Partition Key + Sort Key) [cite: 31-33].
* [cite_start]**Global Secondary Indexes (GSI)**: Efficient querying on non-key attributes [cite: 41-43].
* [cite_start]**Conditional Updates**: Prevents data overwrites with attribute-based conditions[cite: 93].
* [cite_start]**Batch Operations**: High-throughput data ingestion using `batch_writer`[cite: 126].
* [cite_start]**ACID Transactions**: Ensures data integrity across multiple operations[cite: 134].
* [cite_start]**Pagination**: Built-in support for scanning large datasets using `LastEvaluatedKey`[cite: 116].
* [cite_start]**Centralized Error Handling**: Custom management for AWS-specific exceptions like `ProvisionedThroughputExceededException`[cite: 156].

## 📂 Project Structure

The project is modularized to separate concerns:
```text
Practical_4_dynamodb/
├── dynamodb_module/
│   ├── __init__.py
│   ├── batch_operations.py      # Logic for batch_put_item
│   ├── config.py                # AWS resource and client initialization
│   ├── crud_operations.py       # Standard Put, Get, Update, Delete, Query
│   ├── error_handler.py         # AWS exception logic and retries
│   ├── table_manager.py         # Table creation and GSI configuration
│   └── transaction_operations.py # TransactWriteItems implementation
└── main.py                      # Application entry point
[cite_start]
http://googleusercontent.com/immersive_entry_chip/0

### Configuration
[cite_start]The project is configured to use the `ap-south-1` (Mumbai) region by default[cite: 21]. You can modify this in `dynamodb_module/config.py`.

## 💻 Usage Examples

### 1. Conditional Updates
Updates marks only if the new value meets specific criteria, ensuring data consistency:
```python
update_marks(student_id="S101", course_id="C001", new_marks=90)

http://googleusercontent.com/immersive_entry_chip/1
http://googleusercontent.com/immersive_entry_chip/2
http://googleusercontent.com/immersive_entry_chip/3

---

### A Few Quick Observations from your Code:
* **Efficiency**: In your `crud_operations.py`, you used `ConditionExpression="marks <:m"`[cite: 93]. This is a great "production-lean" touch—it ensures you aren't accidentally downgrading a student's score if a stale update request comes in.
* **Reliability**: Your `error_handler.py` includes a `time.sleep(2)` for throughput exceptions[cite: 158]. While simple, this manual backoff is exactly what's needed to handle "bursty" traffic in DynamoDB.

How are you planning to handle the AWS credentials for this repo—are you using an IAM role or local environment variables?
