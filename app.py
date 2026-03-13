import streamlit as st
import random
import time
from PIL import Image

def main():

    st.set_page_config(page_title="AgriVision AI", layout="wide")
   st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"]{
background-color:#0f3d0f;
color:white;
}

/* HEADER */
[data-testid="stHeader"]{
background:transparent;
}

/* WHITE CARDS */
div[data-testid="stMetric"],
div[data-testid="stAlert"],
div[data-testid="stVerticalBlock"] > div {
background-color:white;
color:#1b5e20;
padding:15px;
border-radius:12px;
margin-bottom:10px;
}

/* BUTTON STYLE */
.stButton > button {
background-color:#4CAF50;
color:white;
border-radius:8px;
border:none;
padding:8px 16px;
}

/* HEADINGS */
h1,h2,h3,h4{
color:white;
}

</style>
""", unsafe_allow_html=True)

    st.title("🌱 AgriVision AI")

    st.image(
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
        width=700
    )

    st.markdown("An AI-powered smart agriculture monitoring system")

    # -------------------------------
    # 1. Crop Health Detection
    # -------------------------------

    st.header("1. Crop Health Detection")

    uploaded_file = st.file_uploader("Upload a crop image")

    crop_action = "Awaiting image input..."

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Crop Image", use_container_width=True)

        diseases = ["Healthy Leaf", "Leaf Blight", "Powdery Mildew", "Bacterial Spot"]

        prediction = random.choice(diseases)

        confidence = random.randint(88, 97)

        st.subheader("🌿 AI Crop Health Prediction")

        st.write("Predicted Condition:", prediction)

        st.write("AI Confidence:", confidence, "%")

        if prediction != "Healthy Leaf":

            st.error("⚠ Disease detected. Recommended action: Apply organic pesticide.")

            crop_action = "Apply pesticide treatment"

        else:

            st.success("✅ Crop appears healthy.")

            crop_action = "No action required"


    # -------------------------------
    # 2. Soil Moisture Monitoring
    # -------------------------------

    st.header("💧 2. Soil Moisture Monitoring")

    if 'moisture_level' not in st.session_state:

        st.session_state.moisture_level = random.randint(15, 60)

    if st.button("Refresh Moisture Sensor Data"):

        st.session_state.moisture_level = random.randint(15, 60)

    moisture_level = st.session_state.moisture_level

    st.metric(label="Average Soil Moisture", value=f"{moisture_level}%")

    if moisture_level < 30:

        st.warning(f"⚠ Warning: Soil moisture is {moisture_level}% (below 30%). Irrigation is required.")

        irrigation_action = "Start Irrigation"

    else:

        st.success(f"💧 Soil moisture is {moisture_level}%. No irrigation needed.")

        irrigation_action = "No irrigation required"


    # -------------------------------
    # 3. Field Monitoring Status
    # -------------------------------

    st.header("3. Field Monitoring Status")

    st.markdown("### Sector Status Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("**Sector A (North)**\n\nStatus: Healthy")

    with col2:
        st.warning("**Sector B (South)**\n\nStatus: Needs Water")

    with col3:
        st.error("**Sector C (East)**\n\nStatus: Pest Detection")

    with col4:
        st.success("**Sector D (West)**\n\nStatus: Healthy")


    # -------------------------------
    # 4. Smart Agriculture Alerts
    # -------------------------------

    st.header("4. Smart Agriculture Alerts")

    st.write(f"**Crop Action:** {crop_action}")

    st.write(f"**Irrigation Action:** {irrigation_action}")


    # -------------------------------
    # 5. Smart Farm Monitoring Simulation
    # -------------------------------

    st.header("🌾 5. Smart Farm Monitoring Simulation")

    if st.button("Simulate Field Monitoring"):

        activity_log = st.empty()

        with activity_log.container():

            st.write("🌱 Initializing smart field monitoring system...")

            time.sleep(1)

            st.write("📷 Analyzing crop images and detecting plant health...")

            time.sleep(1.5)

            st.write("🧠 Running AI analysis on crop and soil data...")

            time.sleep(1.5)

            st.write("📊 Updating smart agriculture dashboard...")

            time.sleep(1)

            st.success("✅ Monitoring complete. Smart agriculture system updated.")


if __name__ == "__main__":
    main()
