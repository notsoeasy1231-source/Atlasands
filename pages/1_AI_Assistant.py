import streamlit as st
from openai import OpenAI
from data.prompts import TRAVEL_ASSISTANT_PROMPT

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Travel Assistant",
    page_icon="🤖",
    layout="wide"
)

col1, col2 = st.columns([1, 5])

with col1:
    st.image("assets/icons/ai.png", width=70)

with col2:
    st.title("AI Travel Assistant")
    st.caption("Your smart travel companion for exploring India.")
st.caption("Ask anything about planning trips across India!")

# -----------------------------
# OpenAI Client
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
user_prompt = st.chat_input(
    "Example: I have ₹20,000 and 5 days. Suggest a trip from Hyderabad."
)

if user_prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # -----------------------------
    # System Prompt
    # -----------------------------
    system_prompt = """
You are ATLASANDS AI, an expert travel assistant for INDIA ONLY.

You help users with:
- Trip planning
- Itineraries
- Budgets
- Hill stations
- Beaches
- Wildlife
- Heritage
- Spiritual tourism
- Restaurants
- Transportation
- Packing lists
- Hidden gems
- Scenic viewpoints
- Family trips
- Solo trips
- Adventure travel
- Weekend getaways
- Travel safety
- Local food

If a user asks about coding, politics, medicine, mathematics,
or anything unrelated to Indian travel, politely refuse and
redirect the conversation back to travel planning.

Always give practical, friendly, and easy-to-understand answers.
"""

    # -----------------------------
    # Generate Response
    # -----------------------------
    with st.chat_message("assistant"):

        with st.spinner("Planning your trip..."):

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    *st.session_state.messages
                ]
            )

            reply = response.choices[0].message.content

            st.markdown(reply)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🌍 ATLASANDS")
st.sidebar.image("assets/icons/ai.png", width=60)
st.sidebar.markdown("### AI Assistant")
st.sidebar.info(
    """
Try asking:

• Plan a 4-day Kerala trip

• Best hill stations under ₹15,000

• Packing list for Ladakh

• Hidden gems near Jaipur

• Family vacation ideas

• Vegetarian food recommendations in Goa
"""
)

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

