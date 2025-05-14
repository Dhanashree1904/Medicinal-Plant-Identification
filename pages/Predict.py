import streamlit as st
from utils import load_model, predict_image, get_plant_details, save_history

model, class_names = load_model("best_mobilenet_model.h5")
plant_df = get_plant_details("plant_details.csv")

st.title("🔍 Prediction")

# Apply custom styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "img" not in st.session_state or st.session_state.img is None:
    st.warning("Please upload a plant image from the Home page.")
    st.stop()

img = st.session_state.img
prediction, confidence = predict_image(img, model, class_names)
st.session_state.prediction = prediction

save_history(st.session_state.user, prediction, img)

col1, col2 = st.columns(2)

with col1:
    st.image(img, use_container_width=True)
    # st.success(f"**Prediction:** {prediction} ({confidence:.2%} confidence)")

with col2:
    # Show CSV plant details
    plant_info = plant_df[plant_df["Common Name"].str.lower() == prediction.lower()]
    if not plant_info.empty:
        st.subheader("Plant Details")
        for k, v in plant_info.iloc[0].to_dict().items():
            st.write(f"**{k}:** {v}")
    else:
        st.info("No additional information found for this plant.")

if st.button("⬅️ Back to Home"):
    st.switch_page("pages/Home.py")



