import requests
from config import TELEGRAM_BOT_TOKEN, ADMIN_CHAT_ID

def send_order_to_admin(order_id, order):
    text = f"""
📌 New Order Received
User: {order['user_id']}
Game: {order['game']}
Package: {order['package']}
Account ID: {order['account_id']}
Server ID: {order.get('server_id', 'N/A')}
"""
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "✅ Approve", "callback_data": f"approve:{order_id}"},
                {"text": "❌ Reject", "callback_data": f"reject:{order_id}"}
            ]
        ]
    }
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": ADMIN_CHAT_ID, "text": text, "reply_markup": keyboard})

def send_message_to_user(user_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": user_id, "text": text})
