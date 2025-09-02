from flask import Blueprint, jsonify
from models.task_model import get_special_tasks

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/daily", methods=["GET"])
def daily_tasks():
    return jsonify({"watch_ad_limit": 20})

@task_bp.route("/special", methods=["GET"])
def special_tasks():
    tasks = get_special_tasks()
    return jsonify({"tasks": tasks})
