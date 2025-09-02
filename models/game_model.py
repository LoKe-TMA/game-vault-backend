PUBG_PACKAGES = [
    {"type": "UC 60", "price": 4500},
    {"type": "UC 180", "price": 13500},
    {"type": "UC 325", "price": 21000},
    {"type": "UC 385", "price": 25500},
    {"type": "UC 660", "price": 41000},
    {"type": "UC 720", "price": 45000},
    {"type": "UC 985", "price": 61000},
    {"type": "UC 1800", "price": 100000}
]

MLBB_PACKAGES = [
    {"type": "Weekly Pass", "price": 6500},
    {"type": "Diamond 86", "price": 5500},
    {"type": "Diamond 172", "price": 11000},
    {"type": "Diamond 257", "price": 16500},
    {"type": "Diamond 343", "price": 21500},
    {"type": "Diamond 429", "price": 27000},
    {"type": "Diamond 706", "price": 43000},
    {"type": "Diamond 1049", "price": 63000}
]

def get_games():
    return {
        "PUBG": {"logo": "https://example.com/pubg.png", "packages": PUBG_PACKAGES},
        "MLBB": {"logo": "https://example.com/mlbb.png", "packages": MLBB_PACKAGES}
    }
