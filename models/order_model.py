from config import db
import datetime

orders_col = db["orders"]

def create_order(user_id, game, package, account_id, server_id=None):
    order = {
        "user_id": user_id,
        "game": game,
        "package": package,
        "account_id": account_id,
        "server_id": server_id,
        "status": "pending",
        "created_at": datetime.datetime.utcnow()
    }
    orders_col.insert_one(order)
    return order

def get_orders(user_id):
    return list(orders_col.find({"user_id": user_id}, {"_id": 0}))
