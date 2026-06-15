import streamlit as st

st.title("💾 Saved Trips")

if "saved_trip" in st.session_state:
    st.markdown(st.session_state["saved_trip"])
else:
    st.info("No saved trips yet.")