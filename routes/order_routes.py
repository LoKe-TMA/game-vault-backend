from flask import Blueprint, request, jsonify
from models.order_model import create_order, get_orders
import jwt
from config import JWT_SECRET

order_bp = Blueprint("order", __name__)

def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except:
        return None

@order_bp.route("/create", methods=["POST"])
def create():
    token = request.headers.get("Authorization")
    decoded = decode_token(token)
    if not decoded:
        return jsonify({"error": "Invalid token"}), 401

    data = request.json
    game = data.get("game")
    package = data.get("package")
    account_id = data.get("account_id")
    server_id = data.get("server_id")

    order = create_order(decoded["telegram_id"], game, package, account_id, server_id)
    return jsonify({"message": "Order created", "order": order})

@order_bp.route("/my", methods=["GET"])
def my_orders():
    token = request.headers.get("Authorization")
    decoded = decode_token(token)
    if not decoded:
        return jsonify({"error": "Invalid token"}), 401

    orders = get_orders(decoded["telegram_id"])
    return jsonify({"orders": orders})
