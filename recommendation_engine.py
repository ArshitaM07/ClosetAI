import json


def get_outfit(mood, weather, occasion):

    with open("user_profile.json", "r") as file:
        profile = json.load(file)

    with open("feedback.json", "r") as file:
        feedback = json.load(file)

    with open("favorites.json", "r") as file:
        history = json.load(file)


    favorite_color = profile["favorite_color"]
    style = profile["style"]
    comfort_level = profile["comfort_level"]


    top_options = []

    if style == "minimal":
        top_options = [
            f"{favorite_color} plain shirt",
            f"{favorite_color} polo shirt"
        ]

    elif style == "streetwear":
        top_options = [
            f"{favorite_color} oversized graphic tee",
            f"{favorite_color} hoodie"
        ]

    elif style == "academic":
        top_options = [
            f"{favorite_color} cardigan",
            f"{favorite_color} sweater"
        ]

    else:
        top_options = [
            f"{favorite_color} casual t-shirt",
            f"{favorite_color} shirt"
        ]


    top = top_options[0]

    for option in top_options:
        if option not in str(history):
            top = option
            break


    if comfort_level == "comfortable":
        bottom = "loose joggers"

    elif comfort_level == "balanced":
        bottom = "straight-fit jeans"

    else:
        bottom = "fitted trousers"


    if occasion == "presentation":
        footwear = "formal shoes"
        accessory = "watch"

    elif occasion == "lecture":
        footwear = "white sneakers"
        accessory = "backpack"

    else:
        footwear = "canvas shoes"
        accessory = "tote bag"


    explanation = (
        "personalized based on your style, "
        "comfort preference, and outfit history"
    )


    outfit = (
        f"{top} + "
        f"{bottom} + "
        f"{footwear} + "
        f"{accessory}"
    )

    return outfit, explanation