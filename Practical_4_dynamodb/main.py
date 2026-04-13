from dynamodb_module.table_manager import create_table
from dynamodb_module.crud_operations import insert_item, query_by_student, update_marks,delete_item
from dynamodb_module.batch_operations import batch_insert
from dynamodb_module.transaction_operations import transactional_insert


create_table()

insert_item({
    "student_id": "S101",
    "course_id": "C001",
    "name": "Darshan",
    "status": "active",
    "marks": 85
})

query_by_student("S101")

update_marks("S101", "C001", 90)

batch_insert([
    {
        "student_id": "S102",
        "course_id": "C002",
        "name": "Virendra",
        "status": "active",
        "marks": 75
    },
    {
        "student_id": "S103",
        "course_id": "C003",
        "name": "Rohan",
        "status": "inactive",
        "marks": 80
    }
])

transactional_insert()
delete_item("S101", "C001")
