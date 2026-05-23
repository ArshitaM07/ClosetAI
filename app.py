from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from image_classifier import classify_clothing
from ai_chat import get_ai_reply
import os
import json

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Create files automatically if missing

def create_if_missing():

    if not os.path.exists("wardrobe.json"):

        with open("wardrobe.json", "w") as f:

            json.dump({

                "tops": [],
                "bottoms": [],
                "footwear": [],
                "accessories": []

            }, f, indent=4)


    if not os.path.exists("profile.json"):

        with open("profile.json", "w") as f:

            json.dump({

                "skin_tone":"",
                "body_structure":"",
                "height":"",
                "style":"",
                "comfort":"",
                "favorite_colors":[],
                "avoid_colors":[]

            }, f, indent=4)


create_if_missing()


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/chat", methods=["POST"])
def chat():

    message = request.form.get(
        "message",
        ""
    )

    reply = get_ai_reply(
        message
    )

    return jsonify({

        "reply": reply

    })


@app.route("/upload", methods=["POST"])
def upload():

    if "image" not in request.files:

        return jsonify({

            "message":
            "No image received"

        })

    file = request.files["image"]

    if file.filename == "":

        return jsonify({

            "message":
            "No file selected"

        })


    filename = secure_filename(
        file.filename
    )

    save_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(
        save_path
    )


    category = classify_clothing(
        filename
    )


    with open(
    "wardrobe.json",
    "r"
    ) as f:

        wardrobe = json.load(f)


    item_name = filename.split(".")[0]


    wardrobe[category].append(
        item_name
    )


    with open(
    "wardrobe.json",
    "w"
    ) as f:

        json.dump(
            wardrobe,
            f,
            indent=4
        )


    return jsonify({

        "message":
        f"{item_name} added to {category} ✅"

    })


@app.route("/get_wardrobe")
def get_wardrobe():

    files = []

    for file in os.listdir(
    UPLOAD_FOLDER
    ):

        files.append(
            file
        )

    return jsonify(
        files
    )


@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(

        UPLOAD_FOLDER,
        filename

    )


if __name__ == "__main__":

    app.run(
        debug=True
    )