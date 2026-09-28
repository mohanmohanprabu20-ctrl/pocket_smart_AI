from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

from services.gemini_service import generate_text, generate_with_image

from prompts.home_prompt import home_prompt
from prompts.party_prompt import party_prompt
from prompts.jewelry_prompt import jewelry_prompt


app = Flask(__name__)

CORS(app)

app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------------------
# HOME PLANNER
# -----------------------------------------

@app.route("/generate-home", methods=["POST"])
def generate_home():

    try:

        data = request.get_json()

        room = data.get("room", "")
        budget = data.get("budget", "")
        quantity = data.get("quantity", "")
        style = data.get("style", "")

        if not room or not budget:
            return jsonify({
                "success": False,
                "message": "Room and budget are required."
            }), 400

        prompt = home_prompt(
            room,
            budget,
            quantity,
            style
        )

        result = generate_text(prompt)

        if not result:
            result = default_home_result(budget)

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# -----------------------------------------
# PARTY PLANNER
# -----------------------------------------

@app.route("/generate-party", methods=["POST"])
def generate_party():

    try:

        data = request.get_json()

        event_type = data.get("event_type", "")
        budget = data.get("budget", "")
        guests = data.get("guests", "")
        location = data.get("location", "")

        if not event_type or not budget or not guests:
            return jsonify({
                "success": False,
                "message": "Event, budget and guest count are required."
            }), 400

        prompt = party_prompt(
            event_type,
            budget,
            guests,
            location
        )

        result = generate_text(prompt)

        if not result:
            result = default_party_result(budget, guests)

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# -----------------------------------------
# JEWELRY PLANNER
# -----------------------------------------

@app.route("/generate-jewelry", methods=["POST"])
def generate_jewelry():

    try:

        budget = request.form.get("budget")
        occasion = request.form.get("occasion")
        outfit = request.form.get("outfit", "")

        image = request.files.get("image")

        if not budget or not occasion:
            return jsonify({
                "success": False,
                "message": "Budget and occasion are required."
            }), 400

        prompt = jewelry_prompt(
            budget,
            occasion,
            outfit
        )

        if image:

            result = generate_with_image(
                prompt,
                image
            )

        else:

            result = generate_text(prompt)

        if not result:
            result = default_jewelry_result(budget)

        return jsonify({
            "success": True,
            "result": result
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# -----------------------------------------
# FALLBACK RESULTS
# -----------------------------------------

def default_home_result(budget):

    return f"""
HOME PLAN

Budget: ₹{budget}

Recommended categories:

1. Lighting
2. Curtains
3. Storage
4. Wall Decor
5. Furniture
6. Indoor Plants

AI service is temporarily unavailable.
Please try again later.

Budget Status:
Manual planning required.
"""


def default_party_result(budget, guests):

    return f"""
PARTY PLAN

Budget: ₹{budget}

Guests: {guests}

Suggested allocation:

Food: 50%
Decoration: 15%
Cake: 10%
Entertainment: 10%
Photography: 5%
Miscellaneous: 10%

AI service is temporarily unavailable.
Please try again later.
"""


def default_jewelry_result(budget):

    return f"""
JEWELRY PLAN

Budget: ₹{budget}

Suggested categories:

Necklace
Earrings
Bracelet/Bangles
Ring

AI service is temporarily unavailable.
Please try again later.
"""


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )