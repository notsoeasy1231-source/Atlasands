import streamlit as st
from openai import OpenAI

st.title("🎒 Packing Assistant")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

destination = st.text_input("Destination")
season = st.selectbox(
    "Season",
    ["Summer", "Winter", "Monsoon"]
)
activities = st.text_input("Activities")

if st.button("Generate Packing List"):

    prompt = f"""
Create a packing list.

Destination: {destination}
Season: {season}
Activities: {activities}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.markdown(response.choices[0].message.content)