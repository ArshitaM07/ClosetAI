from PIL import Image

def classify_clothing(filename):

    filename = filename.lower()

    tops = [
        "shirt",
        "tshirt",
        "hoodie",
        "top",
        "sweater"
    ]

    bottoms = [
        "jeans",
        "pant",
        "trouser",
        "shorts"
    ]

    footwear = [
        "shoe",
        "sneaker",
        "boot",
        "heel"
    ]

    accessories = [
        "bag",
        "watch",
        "cap"
    ]


    for item in tops:
        if item in filename:
            return "tops"

    for item in bottoms:
        if item in filename:
            return "bottoms"

    for item in footwear:
        if item in filename:
            return "footwear"

    for item in accessories:
        if item in filename:
            return "accessories"

    return "tops"