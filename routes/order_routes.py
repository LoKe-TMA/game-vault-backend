from flask import Blueprint, request, jsonify
from models.order_model import create_order, update_order_status
from models.user_model import update_coins
from admin_notify import send_order_to_admin, send_message_to_user
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
    order = create_order(
        decoded["telegram_id"],
        data.get("game"),
        data.get("package"),
        data.get("account_id"),
        data.get("server_id")
    )

    send_order_to_admin(order["_id"], order)
    return jsonify({"message": "Order created and sent to admin", "order": order})

@order_bp.route("/admin/callback", methods=["POST"])
def admin_callback():
    data = request.json
    callback_data = data.get("callback_query")
    action, order_id = callback_data["data"].split(":")
    user_id = callback_data["from"]["id"]

    order = get_order_by_id(order_id)
    if not order:
        return "Order not found", 404

    if action == "approve":
        update_order_status(order_id, "approved")
        # Deduct coins
        price = 0
        if order["game"] == "PUBG":
            from models.game_model import get_pubg_packages
            price = next(p["price"] for p in get_pubg_packages() if p["type"]==order["package"])
        else:
            from models.game_model import get_mlbb_packages
            price = next(p["price"] for p in get_mlbb_packages() if p["type"]==order["package"])
        update_coins(order["user_id"], -price)
        send_message_to_user(order["user_id"], "✅ Order Approved")
    else:
        update_order_status(order_id, "rejected")
        send_message_to_user(order["user_id"], "❌ Order Rejected")
    return "ok"
