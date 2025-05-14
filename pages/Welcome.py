import streamlit as st

# Set up the page
st.set_page_config(page_title="Welcome | Medicinal Plant ID", layout="centered")

# Apply custom styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Welcome screen content
st.markdown("""
<div style='text-align: center; padding: 2rem 1rem;'>
    <h1 style='font-size: 3rem;'>🌿 Welcome to Medicinal Plant Identifier</h1>
    <p style='font-size: 1.2rem; margin-top: 1rem;'>
        Upload a plant image and discover its name and medicinal benefits instantly.
    </p>
</div>
""", unsafe_allow_html=True)

# Use a real button with Streamlit navigation
st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
if st.button("👉 Get Started"):
    st.switch_page("app.py")
st.markdown("</div>", unsafe_allow_html=True)

# import streamlit as st

# with open("styles.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# st.set_page_config(page_title="Welcome - Medicinal Plant ID", layout="centered")

# st.markdown("## 🌿 Welcome!")
# st.markdown("Upload your images and get started with identifying medicinal plants.")
# st.image("https://cdn.pixabay.com/photo/2017/07/21/20/30/plant-2522533_960_720.jpg", use_column_width=True)

# if st.button("🔐 Login / Signup"):
#     st.switch_page("app.py")  # Note: this only works if running Streamlit 1.22+, otherwise redirect to Home/Login manually



# # pages/Welcome.py

# import streamlit as st

# st.set_page_config(page_title="Welcome", layout="centered")

# # Apply custom styling
# with open("assets/style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Welcome content
# st.markdown("## 🌿 Welcome to the Medicinal Plant Identification System!")
# st.markdown("Upload your plant images and get detailed information instantly.")

# st.image("https://cdn.pixabay.com/photo/2017/07/17/22/23/herbs-2510963_1280.jpg", use_column_width=True)

# st.markdown("### Get Started:")
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("🔐 Login"):
#         st.switch_page("pages/LoginSignup.py")
# with col2:
#     if st.button("📝 Sign Up"):
#         st.switch_page("pages/LoginSignup.py")
