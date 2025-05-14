import streamlit as st
from utils import get_history, decode_image, delete_history, get_plant_details
from bson.objectid import ObjectId

st.title("🕓 Prediction History")

# Apply custom styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Back to Home button at the top
if st.button("⬅️ Back to Home"):
    st.switch_page("pages/Home.py")

plant_df = get_plant_details("plant_details.csv")
history = get_history(st.session_state.user)

if not history:
    st.info("No prediction history found.")
    st.stop()

for record in reversed(history):
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column widths
    with col1:
        st.image(decode_image(record["image"]), use_container_width=True)
    with col2:
        st.write(f"**Prediction:** {record['prediction']}")
        plant_info = plant_df[plant_df["Common Name"].str.lower() == record['prediction'].lower()]
        if not plant_info.empty:
            st.subheader("🌱 Details:")
            for k, v in plant_info.iloc[0].to_dict().items():
                st.write(f"**{k}:** {v}")
        else:
            st.info("No details found for this plant.")
    with col3:
        if st.button("🗑 Delete", key=str(record["_id"])):
            delete_history(ObjectId(record["_id"]))
            st.rerun()
        st.empty() # Add an empty element to potentially align the next item