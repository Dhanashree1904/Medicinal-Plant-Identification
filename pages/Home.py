import streamlit as st
from PIL import Image

st.title("Welcome!")

# Apply custom styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("Upload an image of a medicinal plant to get started!")

# Style the file uploader
st.markdown(
    """
    <style>
    .st-file-uploader {
        background-color: white !important;
        border: 1px solid #b0b0b0 !important;
        border-radius: 6px !important;
        padding: 10px !important;
    }
    div.stButton > button:nth-child(3) { /* Target the Logout button */
        background-color: #ff4b4b !important; /* Red background */
        color: white !important;
    }
    div.stButton > button {
        width: 100%; /* Make buttons take full width of their container */
    }
    @media (min-width: 600px) {
        div.stButton > button {
            max-width: 200px; /* Set a maximum width for consistent size on larger screens */
        }
        div[style*="flex-direction: row;"] > div:first-child div.stButton > button {
            width: auto; /* Adjust width for the History button in the flex container */
        }
        div[style*="flex-direction: row;"] > div:last-child div.stButton > button {
            width: auto; /* Adjust width for the Logout button in the flex container */
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)
uploaded_file = st.file_uploader("Upload plant image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.session_state.img = image

    if st.button("🔍 Predict This Plant"):
        st.switch_page("pages/Predict.py")

# Navigation buttons
st.divider()
st.markdown("<div style='display: flex; justify-content: space-between;'>", unsafe_allow_html=True)
if st.button("View History"):
    st.switch_page("pages/History.py")
if st.button("Logout"):
    st.switch_page("pages/Logout.py")
st.markdown("</div>", unsafe_allow_html=True)