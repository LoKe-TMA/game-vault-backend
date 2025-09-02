from config import db

special_tasks_col = db["special_tasks"]

def get_special_tasks():
    return list(special_tasks_col.find({}, {"_id": 0}))

def add_special_task(task):
    special_tasks_col.insert_one(task)
