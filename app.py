import streamlit as st
import os
import random
from pathlib import Path
from data.destinations import DESTINATIONS
from pathlib import Path

css_path = Path("styles/style.css")

if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="ATLASANDS",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"] {
    font-family: "Poppins", sans-serif;
}

.stApp{
    background: linear-gradient(
        135deg,
        #07121d,
        #0d1b2a,
        #12263a
    );
}

/* Hero card */

.hero{
    padding:40px;
    border-radius:30px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,0.2);
}

/* Feature cards */

.card{
    padding:25px;
    border-radius:20px;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(12px);
    transition:0.3s;
}

.card:hover{
    transform:translateY(-6px);
}

h1,h2,h3{
    color:white;
}

p{
    color:#d8d8d8;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD RANDOM HERO IMAGE
# ---------------------------------------------------

hero_folder = Path("assets/hero")

hero_images = []

if hero_folder.exists():

    hero_images = list(hero_folder.glob("*.jpg")) + \
                  list(hero_folder.glob("*.png")) + \
                  list(hero_folder.glob("*.jpeg"))

hero_image = None

if hero_images:
    hero_image = random.choice(hero_images)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("🌍 ATLASANDS")

budget = st.sidebar.slider(
    "Budget (₹)",
    5000,
    200000,
    30000,
    step=5000
)

days = st.sidebar.slider(
    "Travel Days",
    1,
    15,
    5
)

travel_style = st.sidebar.selectbox(
    "Travel Style",
    [
        "Solo",
        "Couple",
        "Family",
        "Friends",
        "Luxury"
    ]
)

category = st.sidebar.selectbox(
    "Destination Type",
    [
        "Any",
        "Beach",
        "Hill Station",
        "Adventure",
        "Wildlife",
        "Heritage",
        "Spiritual"
    ]
)

weather = st.sidebar.selectbox(
    "Preferred Weather",
    [
        "Cool",
        "Snow",
        "Pleasant",
        "Sunny",
        "Rainy"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    f"""
Budget : ₹{budget:,}

Days : {days}

Style : {travel_style}
"""
)

# ---------------------------------------------------
# NAVBAR
# ---------------------------------------------------

col1,col2,col3,col4,col5=st.columns([4,1,1,1,1])

with col1:
    st.markdown(
        "## 🌍 ATLASANDS"
    )

with col2:
    st.write("Home")

with col3:
    st.write("Explore")

with col4:
    st.write("AI Planner")

with col5:
    st.write("About")

st.markdown("---")

# ---------------------------------------------------
# HERO SECTION
# ---------------------------------------------------

if hero_image:

    st.image(
        str(hero_image),
        use_container_width=True
    )

st.markdown(
    """
# Explore India with AI ✨

### Your intelligent travel companion for unforgettable journeys.

Plan personalized trips, optimize budgets, discover hidden gems,
and create memories with the power of AI.
"""
)

c1, c2 = st.columns(2)

with c1:

    if st.button(
        "🚀 Plan My Trip",
        use_container_width=True
    ):
        st.switch_page("pages/2_Smart_Trip_Planner.py")

with c2:

    if st.button(
        "🤖 Chat with AI",
        use_container_width=True
    ):
        st.switch_page("pages/1_AI_Assistant.py")

st.markdown("---")
st.info(
    "✨ Welcome to ATLASANDS! Plan smarter, travel better, and discover amazing destinations across India with AI-powered recommendations."
)

# ---------------------------------------------------
# WHY CHOOSE US
# ---------------------------------------------------

st.header("✨ Why Choose ATLASANDS")

a,b,c,d=st.columns(4)

with a:
    st.markdown("""
<div class="card">
<h3>🤖 AI Planner</h3>
<p>Create personalized itineraries in seconds.</p>
</div>
""",unsafe_allow_html=True)

with b:
    st.markdown("""
<div class="card">
<h3>💰 Budget Friendly</h3>
<p>Travel smarter while staying within budget.</p>
</div>
""",unsafe_allow_html=True)

with c:
    st.markdown("""
<div class="card">
<h3>💎 Hidden Gems</h3>
<p>Discover places beyond the tourist hotspots.</p>
</div>
""",unsafe_allow_html=True)

with d:
    st.markdown("""
<div class="card">
<h3>🎒 Smart Packing</h3>
<p>Receive AI-generated packing suggestions.</p>
</div>
""",unsafe_allow_html=True)
st.markdown("## 🔍 Search Destinations")

search = st.text_input(
    "Search by destination name",
    placeholder="e.g. Goa, Kashmir, Darjeeling"
)

if search:
    matches = [
        d for d in DESTINATIONS
        if search.lower() in d["name"].lower()
    ]

    if matches:
        cols = st.columns(3)
        for i, d in enumerate(matches):
            with cols[i % 3]:
                st.image(d["image"], use_container_width=True)
                st.subheader(d["name"])
                st.caption(d["state"])
                st.write(d["category"])
    else:
        st.warning("No destinations found.")
        st.markdown("## 🎲 Feeling Adventurous?")

# ---------------------------------------------------
# FEATURED DESTINATIONS
# ---------------------------------------------------

st.markdown("## 🏞️ Featured Destinations")
st.caption("Explore some of India's most beautiful places.")

featured = [
    {
        "name": "Goa",
        "budget": "₹18k",
        "season": "Nov - Feb",
        "image": "assets/destinations/goa.jpg"
    },
    {
        "name": "Manali",
        "budget": "₹22k",
        "season": "Oct - Jun",
        "image": "assets/destinations/manali.jpg"
    },
    {
        "name": "Jaipur",
        "budget": "₹15k",
        "season": "Oct - Mar",
        "image": "assets/destinations/jaipur.jpg"
    },
    {
        "name": "Ladakh",
        "budget": "₹35k",
        "season": "May - Sep",
        "image": "assets/destinations/ladakh.jpg"
    },
    {
        "name": "Kerala",
        "budget": "₹20k",
        "season": "Sep - Mar",
        "image": "assets/destinations/kerala.jpg"
    },
    {
        "name": "Rishikesh",
        "budget": "₹12k",
        "season": "All Year",
        "image": "assets/destinations/rishikesh.jpg"
    }
]

cols = st.columns(3)

for i, place in enumerate(featured):
    with cols[i % 3]:

        if os.path.exists(place["image"]):
            st.image(place["image"], use_container_width=True)

        st.markdown(f"### 📍 {place['name']}")
        st.write(f"💰 Budget: {place['budget']}")
        st.write(f"🌤️ Best Season: {place['season']}")

        st.button(
            f"Explore {place['name']}",
            key=place["name"]
        )

st.markdown("---")
st.markdown("## 🎲 Feeling Adventurous?")
st.markdown("## 🌍 Explore All Destinations")

with st.expander("Click to view all destinations"):
    cols = st.columns(3)

    for i, d in enumerate(DESTINATIONS):
        with cols[i % 3]:
            st.image(d["image"], use_container_width=True)
            st.subheader(d["name"])
            st.caption(d["state"])
            st.write(f"🏷️ {d['category']}")
if st.button("Surprise Me ✨"):
    place = random.choice(DESTINATIONS)

    st.success(f"How about visiting **{place['name']}**?")

    st.image(place["image"], use_container_width=True)

    st.write(f"📍 {place['state']}")
    st.write(f"🏷️ {place['category']}")
# ---------------------------------------------------
# AI FEATURES
# ---------------------------------------------------

st.markdown("## AI-Powered Features")

col1, col2 = st.columns([1, 8])

with col1:
    st.image("assets/icons/ai.png", width=50)

with col2:
    st.subheader("AI Travel Assistant")
    st.write("Get personalized travel recommendations powered by AI.")

feature_cols = st.columns(4)

features = [
    ("🗺️", "AI Itinerary"),
    ("💰", "Budget Optimizer"),
    ("🎒", "Packing Assistant"),
    ("💬", "Travel Chat"),
    ("🍽️", "Restaurant Finder"),
    ("📷", "Hidden Gems"),
    ("🚗", "Route Planner"),
    ("📝", "Travel Journal")
]

for i, (emoji, title) in enumerate(features):
    with feature_cols[i % 4]:
        st.markdown(
            f"""
            <div class="card">
                <h3>{emoji}</h3>
                <h4>{title}</h4>
                <p>Powered by AI for a smarter travel experience.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

# ---------------------------------------------------
# QUICK STATS
# ---------------------------------------------------

st.markdown("## 📊 Why Travelers Love ATLASANDS")

s1, s2, s3, s4 = st.columns(4)

s1.metric("Destinations", "35+")
s2.metric("Hero Images", "20")
s3.metric("AI Features", "10+")
s4.metric("Travel Styles", "5")

st.markdown("---")

# ---------------------------------------------------
# TESTIMONIALS
# ---------------------------------------------------

st.markdown("## 💬 What Our Travelers Say")

t1, t2, t3 = st.columns(3)

with t1:
    st.info(
        """
★★★★★

"ATLASANDS planned my entire Himachal trip in seconds.
Everything felt organized and stress-free!"
"""
    )

with t2:
    st.success(
        """
★★★★★

"The budget suggestions were incredibly useful.
I saved money without missing great experiences."
"""
    )

with t3:
    st.warning(
        """
★★★★★

"I loved the itinerary and hidden gem recommendations.
Will definitely use it again!"
"""
    )

st.markdown("---")

# ---------------------------------------------------
# CALL TO ACTION
# ---------------------------------------------------

st.markdown(
    """
# ✨ Ready for Your Next Adventure?

Discover India's most beautiful destinations with the power of AI.
"""
)

if st.button(
    "🌍 Start Planning Now",
    use_container_width=True
):
    st.switch_page("pages/2_Smart_Trip_Planner.py")

st.markdown("---")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
<div style="text-align:center; padding:20px; opacity:0.8;">
<h3>🌍 ATLASANDS</h3>

<p>Your AI Travel Companion for Incredible Journeys Across India.</p>

<p>
Made with ❤️ using Streamlit & OpenAI
</p>

<p>
© 2026 ATLASANDS. All Rights Reserved.
</p>
</div>
""",
    unsafe_allow_html=True
)
