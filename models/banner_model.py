from config import db

banners_col = db["banners"]

def get_all_banners():
    return list(banners_col.find({}, {"_id": 0}))

def add_banner(image_url, click_url):
    banners_col.insert_one({"image_url": image_url, "click_url": click_url})
