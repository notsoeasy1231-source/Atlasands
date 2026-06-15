import streamlit as st
from openai import OpenAI

st.title("📝 AI Travel Journal")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

notes = st.text_area("Describe your trip")

if st.button("Generate Journal"):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": f"Write a beautiful travel journal based on: {notes}"
            }
        ]
    )

    st.markdown(response.choices[0].message.content)