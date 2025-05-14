import streamlit as st

# Apply custom styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.session_state.user = None
st.session_state.img = None
st.session_state.prediction = None

st.success("You have been logged out.")
st.switch_page("pages/Welcome.py")
