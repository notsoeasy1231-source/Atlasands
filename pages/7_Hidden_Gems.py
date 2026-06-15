import streamlit as st

st.title("💎 Hidden Gems")

gems = [
    "Araku Valley",
    "Spiti Valley",
    "Auli",
    "Varkala",
    "Coorg",
    "Munnar",
    "Kaziranga",
    "Shillong"
]

for gem in gems:
    st.success(gem)