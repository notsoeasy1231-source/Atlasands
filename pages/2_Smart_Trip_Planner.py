import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Smart Trip Planner", page_icon="🗺️")

st.title("🗺️ Smart Trip Planner")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

start_city = st.text_input("Starting City")
budget = st.number_input("Budget (₹)", min_value=1000, value=20000)
days = st.slider("Number of Days", 1, 15, 5)

travel_style = st.selectbox(
    "Travel Style",
    ["Solo", "Couple", "Family", "Friends", "Luxury"]
)

interests = st.multiselect(
    "Interests",
    [
        "Beaches",
        "Mountains",
        "Adventure",
        "Wildlife",
        "Heritage",
        "Food",
        "Spiritual",
        "Photography"
    ]
)

if st.button("✨ Generate AI Itinerary"):

    prompt = f"""
Create a realistic India travel itinerary.

Starting city: {start_city}
Budget: ₹{budget}
Days: {days}
Travel style: {travel_style}
Interests: {', '.join(interests)}

Include:
- Day-wise plan
- Places to visit
- Estimated costs
- Food suggestions
- Travel tips
"""

    with st.spinner("Planning..."):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an India travel planner."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

    itinerary = response.choices[0].message.content

    st.markdown(itinerary)

    if st.button("💾 Save Trip"):
        st.session_state["saved_trip"] = itinerary
        st.success("Trip saved!")