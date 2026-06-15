import streamlit as st

st.set_page_config(page_title="Expense Tracker")

st.title("💰 Expense Tracker")

budget = st.number_input("Total Budget (₹)", value=20000)

hotel = st.number_input("Hotel", value=0)
food = st.number_input("Food", value=0)
transport = st.number_input("Transport", value=0)
shopping = st.number_input("Shopping", value=0)
other = st.number_input("Other", value=0)

spent = hotel + food + transport + shopping + other

remaining = budget - spent

st.metric("Spent", f"₹{spent}")
st.metric("Remaining", f"₹{remaining}")

progress = min(spent / budget, 1.0) if budget > 0 else 0
st.progress(progress)