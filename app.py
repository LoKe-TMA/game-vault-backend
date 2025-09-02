from flask import Flask
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.task_routes import task_bp
from routes.refer_routes import refer_bp
from routes.order_routes import order_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(user_bp, url_prefix="/api/user")
app.register_blueprint(task_bp, url_prefix="/api/tasks")
app.register_blueprint(refer_bp, url_prefix="/api/refer")
app.register_blueprint(order_bp, url_prefix="/api/order")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
