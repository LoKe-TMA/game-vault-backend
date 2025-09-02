from flask import Blueprint, request, jsonify
from models.user_model import create_or_get_user
import jwt
from config import JWT_SECRET, TELEGRAM_BOT_TOKEN

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    telegram_id = str(data.get("id"))
    name = data.get("first_name")
    username = data.get("username")

    # TODO: verify Telegram initData HMAC if needed

    user = create_or_get_user(telegram_id, name, username)
    token = jwt.encode({"telegram_id": telegram_id}, JWT_SECRET, algorithm="HS256")
    return jsonify({"token": token, "user": {"name": user["name"], "coins": user["coins"]}})
