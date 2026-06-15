from openai import OpenAI
import streamlit as st

from data.constants import OPENAI_MODEL


def get_openai_client():
    """Create and return an OpenAI client."""
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def generate_ai_response(system_prompt: str, user_prompt: str) -> str:
    """Generate a response using the OpenAI API."""
    client = get_openai_client()

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return response.choices[0].message.content