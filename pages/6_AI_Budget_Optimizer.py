import streamlit as st

st.title("📊 AI Budget Optimizer")

budget = st.number_input("Budget (₹)", value=25000)

hotel = budget * 0.4
food = budget * 0.2
transport = budget * 0.2
activities = budget * 0.15
misc = budget * 0.05

st.write(f"🏨 Hotel: ₹{hotel:.0f}")
st.write(f"🍽️ Food: ₹{food:.0f}")
st.write(f"🚗 Transport: ₹{transport:.0f}")
st.write(f"🎟️ Activities: ₹{activities:.0f}")
st.write(f"📦 Miscellaneous: ₹{misc:.0f}")