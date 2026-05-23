import json
from wardrobe_engine import load_wardrobe


def load_memory():
    try:
        with open("memory.json","r") as file:
            return json.load(file)
    except:
        return {
            "likes":[],
            "dislikes":[],
            "style_preferences":[]
        }


def load_profile():

    try:
        with open("profile.json","r") as file:
            return json.load(file)

    except:
        return {
            "skin_tone":"",
            "body_structure":"",
            "height":"",
            "style":"",
            "comfort":"",
            "favorite_colors":[],
            "avoid_colors":[]
        }


def save_profile(profile):

    with open("profile.json","w") as file:
        json.dump(profile,file,indent=4)


def get_ai_reply(message):

    message=message.lower()

    wardrobe=load_wardrobe()

    profile=load_profile()


    # PROFILE SAVE COMMANDS

    if message.startswith("skin:"):
        profile["skin_tone"]=message.replace("skin:","").strip()
        save_profile(profile)
        return "Skin tone saved ✅"


    if message.startswith("body:"):
        profile["body_structure"]=message.replace("body:","").strip()
        save_profile(profile)
        return "Body structure saved ✅"


    if message.startswith("height:"):
        profile["height"]=message.replace("height:","").strip()
        save_profile(profile)
        return "Height saved ✅"


    if message.startswith("style:"):
        profile["style"]=message.replace("style:","").strip()
        save_profile(profile)
        return "Style preference saved ✅"


    if message.startswith("comfort:"):
        profile["comfort"]=message.replace("comfort:","").strip()
        save_profile(profile)
        return "Comfort preference saved ✅"


    if message.startswith("favorite:"):

        color=message.replace(
            "favorite:",
            ""
        ).strip()

        profile["favorite_colors"].append(
            color
        )

        save_profile(profile)

        return f"{color} saved to favorites ✅"



    if message.startswith("avoid:"):

        color=message.replace(
            "avoid:",
            ""
        ).strip()

        profile["avoid_colors"].append(
            color
        )

        save_profile(profile)

        return f"{color} added to avoid list ✅"



    # Outfit logic

    if "outfit" in message or "wear" in message:

        top=wardrobe["tops"][0] if wardrobe["tops"] else "black hoodie"

        bottom=wardrobe["bottoms"][0] if wardrobe["bottoms"] else "black jeans"

        footwear=wardrobe["footwear"][0] if wardrobe["footwear"] else "white sneakers"

        accessory=wardrobe["accessories"][0] if wardrobe["accessories"] else "backpack"


        return f"""
OUTFIT:

Top:{top}

Bottom:{bottom}

Footwear:{footwear}

Accessory:{accessory}

Why this works:

Style: {profile["style"]}

Comfort: {profile["comfort"]}

Skin tone: {profile["skin_tone"]}

Body structure: {profile["body_structure"]}

Favorite colors:
{profile["favorite_colors"]}

Avoid colors:
{profile["avoid_colors"]}
"""


    return """
Hey 👋

Tell me your mood, weather, or ask for an outfit.
"""