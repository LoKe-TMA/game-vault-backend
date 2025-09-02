from flask import Blueprint, jsonify, request
from models.user_model import get_user
import jwt
from config import JWT_SECRET

refer_bp = Blueprint("refer", __name__)

def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except:
        return None

@refer_bp.route("/info", methods=["GET"])
def refer_info():
    token = request.headers.get("Authorization")
    decoded = decode_token(token)
    if not decoded:
        return jsonify({"error": "Invalid token"}), 401

    user = get_user(decoded["telegram_id"])
    return jsonify({
        "refer_bonus": 100,
        "total_friends": 0,
        "earned_coins": 0
    })
