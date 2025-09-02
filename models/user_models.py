from config import db
import datetime

users_col = db["users"]

def create_or_get_user(telegram_id, name, username):
    user = users_col.find_one({"telegram_id": telegram_id})
    if user:
        return user
    new_user = {
        "telegram_id": telegram_id,
        "name": name,
        "username": username,
        "coins": 0,
        "refer_by": None,
        "created_at": datetime.datetime.utcnow()
    }
    users_col.insert_one(new_user)
    return new_user

def get_user(telegram_id):
    return users_col.find_one({"telegram_id": telegram_id}, {"_id": 0})

def update_coins(telegram_id, amount):
    users_col.update_one({"telegram_id": telegram_id}, {"$inc": {"coins": amount}})
