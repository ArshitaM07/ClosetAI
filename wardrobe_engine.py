import json
import random


def load_wardrobe():

    try:
        with open("wardrobe.json", "r") as file:
            return json.load(file)

    except:
        return {
            "tops": [],
            "bottoms": [],
            "footwear": [],
            "accessories": []
        }


def save_wardrobe(data):

    with open("wardrobe.json", "w") as file:
        json.dump(data, file, indent=4)


def add_item(category, item):

    wardrobe = load_wardrobe()

    if category in wardrobe:
        wardrobe[category].append(item)

    save_wardrobe(wardrobe)


def generate_random_outfit():

    wardrobe = load_wardrobe()

    return {
        "top": random.choice(wardrobe["tops"]) if wardrobe["tops"] else "No top found",

        "bottom": random.choice(wardrobe["bottoms"]) if wardrobe["bottoms"] else "No bottom found",

        "footwear": random.choice(wardrobe["footwear"]) if wardrobe["footwear"] else "No footwear found",

        "accessory": random.choice(wardrobe["accessories"]) if wardrobe["accessories"] else "No accessory found"
    }