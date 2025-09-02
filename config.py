import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/gamevault")
client = MongoClient(MONGO_URI)
db = client["gamevault"]

JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
FLASK_ENV = os.getenv("FLASK_ENV", "production")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADSGRAM_BLOCK_ID = os.getenv("ADSGRAM_BLOCK_ID")
