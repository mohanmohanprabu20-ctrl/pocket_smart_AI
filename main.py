from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import os

from services.gemini_service import (
    generate_text,
    generate_with_image
)

from prompts.home_prompt import home_prompt
from prompts.party_prompt import party_prompt
from prompts.jewelry_prompt import jewelry_prompt


# ==========================================
# FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="Pocket SmartAI",
    description="Your Smart Budget & Recommendation Assistant",
    version="1.0.0"
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ==========================================
# STATIC FILES
# ==========================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# ==========================================
# TEMPLATES
# ==========================================

templates = Jinja2Templates(
    directory="templates"
)


# ==========================================
# UPLOAD DIRECTORY
# ==========================================

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# ==========================================
# HOME PAGE
# ==========================================

@app.get(
    "/",
    response_class=HTMLResponse
)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# ==========================================
# HOME INTERIOR PLANNER
# ==========================================

@app.post("/generate-home")
async def generate_home(data: dict):

    try:

        room = data.get("room", "")
        budget = data.get("budget", "")
        quantity = data.get("quantity", "")
        style = data.get("style", "")


        if not room or not budget:

            return {
                "success": False,
                "message": "Room and budget are required."
            }


        prompt = home_prompt(
            room,
            budget,
            quantity,
            style
        )


        result = generate_text(prompt)


        if not result:

            result = default_home_result(
                budget
            )


        return {
            "success": True,
            "result": result
        }


    except Exception as e:

        print("Home Planner Error:", e)

        return {
            "success": False,
            "message": str(e)
        }


# ==========================================
# PARTY PLANNER
# ==========================================

@app.post("/generate-party")
async def generate_party(data: dict):

    try:

        event_type = data.get(
            "event_type",
            ""
        )

        budget = data.get(
            "budget",
            ""
        )

        guests = data.get(
            "guests",
            ""
        )

        location = data.get(
            "location",
            ""
        )


        if (
            not event_type
            or not budget
            or not guests
        ):

            return {
                "success": False,
                "message":
                    "Event, budget and guests are required."
            }


        prompt = party_prompt(
            event_type,
            budget,
            guests,
            location
        )


        result = generate_text(
            prompt
        )


        if not result:

            result = default_party_result(
                budget,
                guests
            )


        return {
            "success": True,
            "result": result
        }


    except Exception as e:

        print("Party Planner Error:", e)

        return {
            "success": False,
            "message": str(e)
        }


# ==========================================
# JEWELRY PLANNER
# ==========================================

@app.post("/generate-jewelry")
async def generate_jewelry(

    budget: str = Form(...),

    occasion: str = Form(...),

    outfit: str = Form(""),

    image: UploadFile | None = File(None)

):

    try:

        prompt = jewelry_prompt(
            budget,
            occasion,
            outfit
        )


        result = None


        # ----------------------------------
        # IMAGE PROVIDED
        # ----------------------------------

        if image:

            image_bytes = await image.read()

            result = generate_with_image(
                prompt,
                image_bytes
            )


        # ----------------------------------
        # TEXT ONLY
        # ----------------------------------

        else:

            result = generate_text(
                prompt
            )


        if not result:

            result = default_jewelry_result(
                budget
            )


        return {
            "success": True,
            "result": result
        }


    except Exception as e:

        print(
            "Jewelry Planner Error:",
            e
        )

        return {
            "success": False,
            "message": str(e)
        }


# ==========================================
# FALLBACK FUNCTIONS
# ==========================================

def default_home_result(budget):

    return f"""
HOME INTERIOR PLAN

Budget: ₹{budget}

Suggested categories:

1. Lighting
2. Curtains
3. Storage
4. Wall Decor
5. Furniture
6. Indoor Plants

AI recommendation service is
temporarily unavailable.

Please try again later.
"""


def default_party_result(
    budget,
    guests
):

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

AI recommendation service is
temporarily unavailable.
"""


def default_jewelry_result(
    budget
):

    return f"""
JEWELRY PLAN

Budget: ₹{budget}

Suggested categories:

• Necklace
• Earrings
• Bracelet/Bangles
• Ring

AI recommendation service is
temporarily unavailable.
"""