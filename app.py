import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Pocket Smart AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
        .main-title {
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .subtitle {
            font-size: 18px;
            color: #777;
            margin-bottom: 30px;
        }

        .card {
            padding: 25px;
            border-radius: 18px;
            border: 1px solid rgba(128,128,128,0.25);
            margin-top: 20px;
        }

        .result-title {
            font-size: 28px;
            font-weight: 700;
        }

        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">✨ Pocket Smart AI</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Your simple AI planning dashboard</div>',
    unsafe_allow_html=True,
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("✨ Pocket Smart AI")

st.sidebar.write("Choose a planner:")

planner = st.sidebar.radio(
    "",
    [
        "🏠 Home Planner",
        "🎉 Party Planner",
        "💎 Jewelry Planner",
    ],
)

st.sidebar.divider()

st.sidebar.info(
    """
    **Pocket Smart AI**

    • Home planning  
    • Party planning  
    • Jewelry planning  

    Built with Streamlit.
    """
)

# =========================================================
# HOME PLANNER
# =========================================================

def home_planner():

    st.header("🏠 Home Planner")

    st.write(
        "Create a simple home plan based on your room, budget and preferred style."
    )

    col1, col2 = st.columns(2)

    with col1:

        room = st.selectbox(
            "Select Room",
            [
                "Living Room",
                "Bedroom",
                "Kitchen",
                "Dining Room",
                "Study Room",
                "Office",
                "Other",
            ],
        )

        budget = st.number_input(
            "Budget (₹)",
            min_value=0,
            value=50000,
            step=1000,
        )

    with col2:

        requirements = st.text_input(
            "Requirements",
            placeholder="Example: Sofa, TV unit, table",
        )

        style = st.selectbox(
            "Preferred Style",
            [
                "Modern",
                "Minimal",
                "Traditional",
                "Luxury",
                "Industrial",
                "Contemporary",
            ],
        )

    st.divider()

    if st.button(
        "✨ Generate Home Plan",
        type="primary",
        use_container_width=True,
    ):

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="result-title">🏠 Home Plan</div>',
            unsafe_allow_html=True,
        )

        st.write(f"**Room:** {room}")
        st.write(f"**Budget:** ₹{budget:,}")
        st.write(
            f"**Requirements:** {requirements or 'Not specified'}"
        )
        st.write(f"**Style:** {style}")

        st.subheader("Recommended Categories")

        st.write("1. 💡 Lighting")
        st.write("2. 🪟 Curtains")
        st.write("3. 🗄️ Storage")
        st.write("4. 🖼️ Wall Decor")
        st.write("5. 🛋️ Furniture")
        st.write("6. 🪴 Indoor Plants")

        st.subheader("Suggested Budget Distribution")

        st.write("• Furniture — 40%")
        st.write("• Lighting — 15%")
        st.write("• Curtains — 10%")
        st.write("• Storage — 15%")
        st.write("• Decoration — 10%")
        st.write("• Plants / Miscellaneous — 10%")

        st.success("Home plan generated successfully!")

        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PARTY PLANNER
# =========================================================

def party_planner():

    st.header("🎉 Party Planner")

    st.write(
        "Create a party plan based on your event, budget and number of guests."
    )

    col1, col2 = st.columns(2)

    with col1:

        event = st.selectbox(
            "Event Type",
            [
                "Birthday",
                "Wedding",
                "Engagement",
                "Anniversary",
                "College Event",
                "Corporate Event",
                "Other",
            ],
        )

        budget = st.number_input(
            "Budget (₹)",
            min_value=0,
            value=100000,
            step=5000,
        )

    with col2:

        guests = st.number_input(
            "Number of Guests",
            min_value=1,
            value=50,
            step=1,
        )

        location = st.text_input(
            "Location",
            placeholder="Example: Chennai",
        )

    st.divider()

    if st.button(
        "✨ Generate Party Plan",
        type="primary",
        use_container_width=True,
    ):

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="result-title">🎉 Party Plan</div>',
            unsafe_allow_html=True,
        )

        st.write(f"**Event:** {event}")
        st.write(f"**Budget:** ₹{budget:,}")
        st.write(f"**Guests:** {guests}")
        st.write(
            f"**Location:** {location or 'Not specified'}"
        )

        st.subheader("Suggested Budget Allocation")

        food = budget * 0.50
        decoration = budget * 0.15
        cake = budget * 0.10
        entertainment = budget * 0.10
        photography = budget * 0.05
        miscellaneous = budget * 0.10

        st.write(f"🍽️ Food — ₹{food:,.0f}")
        st.write(f"🎈 Decoration — ₹{decoration:,.0f}")
        st.write(f"🎂 Cake — ₹{cake:,.0f}")
        st.write(f"🎵 Entertainment — ₹{entertainment:,.0f}")
        st.write(f"📸 Photography — ₹{photography:,.0f}")
        st.write(f"📦 Miscellaneous — ₹{miscellaneous:,.0f}")

        st.subheader("Planning Checklist")

        st.checkbox("Confirm venue")
        st.checkbox("Finalize guest list")
        st.checkbox("Arrange food")
        st.checkbox("Arrange decoration")
        st.checkbox("Book photographer")
        st.checkbox("Arrange entertainment")

        st.success("Party plan generated successfully!")

        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# JEWELRY PLANNER
# =========================================================

def jewelry_planner():

    st.header("💎 Jewelry Planner")

    st.write(
        "Create a jewelry recommendation based on your budget, occasion and outfit."
    )

    col1, col2 = st.columns(2)

    with col1:

        budget = st.number_input(
            "Budget (₹)",
            min_value=0,
            value=25000,
            step=1000,
        )

        occasion = st.selectbox(
            "Occasion",
            [
                "Wedding",
                "Engagement",
                "Party",
                "Festival",
                "Casual",
                "Formal Event",
                "Other",
            ],
        )

    with col2:

        outfit = st.text_input(
            "Outfit",
            placeholder="Example: Red saree with gold border",
        )

        uploaded_image = st.file_uploader(
            "Upload Outfit Image (Optional)",
            type=[
                "jpg",
                "jpeg",
                "png",
                "webp",
            ],
        )

    if uploaded_image:

        st.image(
            uploaded_image,
            caption="Uploaded Outfit",
            use_container_width=True,
        )

    st.divider()

    if st.button(
        "✨ Generate Jewelry Plan",
        type="primary",
        use_container_width=True,
    ):

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="result-title">💎 Jewelry Plan</div>',
            unsafe_allow_html=True,
        )

        st.write(f"**Budget:** ₹{budget:,}")
        st.write(f"**Occasion:** {occasion}")
        st.write(
            f"**Outfit:** {outfit or 'Not specified'}"
        )

        st.subheader("Recommended Jewelry")

        st.write("💍 Necklace")
        st.write("👂 Earrings")
        st.write("💫 Bracelet / Bangles")
        st.write("💎 Ring")

        st.subheader("Suggested Budget")

        necklace = budget * 0.45
        earrings = budget * 0.25
        bracelet = budget * 0.20
        ring = budget * 0.10

        st.write(f"Necklace — ₹{necklace:,.0f}")
        st.write(f"Earrings — ₹{earrings:,.0f}")
        st.write(f"Bracelet / Bangles — ₹{bracelet:,.0f}")
        st.write(f"Ring — ₹{ring:,.0f}")

        if uploaded_image:
            st.info(
                "Your outfit image was uploaded successfully and can be used as a visual reference."
            )

        st.success("Jewelry plan generated successfully!")

        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# RUN SELECTED PLANNER
# =========================================================

if planner == "🏠 Home Planner":

    home_planner()

elif planner == "🎉 Party Planner":

    party_planner()

elif planner == "💎 Jewelry Planner":

    jewelry_planner()


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "✨ Pocket Smart AI • Powered by Streamlit"
)
