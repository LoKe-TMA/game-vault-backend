from flask import Blueprint, request, jsonify
from models.user_model import get_user
from models.banner_model import get_all_banners
from models.game_model import get_games
import jwt
from config import JWT_SECRET

user_bp = Blueprint("user", __name__)

def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except:
        return None

@user_bp.route("/dashboard", methods=["GET"])
def dashboard():
    token = request.headers.get("Authorization")
    decoded = decode_token(token)
    if not decoded:
        return jsonify({"error": "Invalid token"}), 401

    user = get_user(decoded["telegram_id"])
    banners = get_all_banners()
    games = get_games()

    return jsonify({
        "user": {"name": user["name"], "coins": user["coins"]},
        "banners": banners,
        "games": games
    })
