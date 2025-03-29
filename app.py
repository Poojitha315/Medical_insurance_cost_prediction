import streamlit as st
import pickle
import numpy as np
import time

# Load the trained model
Pkl_Filename = "rf_tuned.pkl"
with open(Pkl_Filename, "rb") as file:
    model = pickle.load(file)

# Apply an animated medical-themed background
page_style = '''
<style>
.stApp {
    background: url('https://www.transparenttextures.com/patterns/cubes.png'), linear-gradient(-45deg, #f0f9ff, #cbeefd, #a6e0fb, #81d4fa);
    background-size: cover;
    animation: gradientAnimation 15s ease infinite;
}

@keyframes gradientAnimation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes heartbeat {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.heartbeat-text {
    animation: heartbeat 1.5s infinite;
    color: black;
    font-weight: bold;
}

h2 {
    color: black !important;
}

.fade-in {
    animation: fadeIn 2s ease-in-out;
    font-size: 18px;
    font-weight: bold;
    color: #004aad;
}

.medical-banner {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #007bff;
    padding: 10px;
}

/* Style input fields and labels */
label {
    color: black !important;
    font-weight: bold;
}

input[type=number], select {
    background-color: black !important;
    color: white !important;
    border: 1px solid #fff !important;
    padding: 10px;
    border-radius: 5px;
}
</style>
'''
st.markdown(page_style, unsafe_allow_html=True)

# Streamlit UI
st.markdown("<div class='medical-banner'>🏥 AI-Powered Medical Cost Prediction 🏥</div>", unsafe_allow_html=True)
st.title("Medical Cost Prediction")
st.write("Enter the required details to predict the expected medical cost.")
st.markdown("<p class='fade-in'>Your health matters! Get an estimate of your medical expenses below.</p>", unsafe_allow_html=True)

# User input fields
age = st.number_input("🧓 Age", min_value=0, max_value=120, step=1)
bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=50.0, step=0.1)
children = st.number_input("👶 Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("🚬 Smoker", ["No", "Yes"])
region = st.selectbox("📍 Region", ["Southwest", "Southeast", "Northwest", "Northeast"])
sex = st.selectbox("⚥ Sex", ["Male", "Female"])

# Convert categorical inputs to numerical
smoker = 1 if smoker == "Yes" else 0
region_map = {"Southwest": 0, "Southeast": 1, "Northwest": 2, "Northeast": 3}
region = region_map[region]
sex = 1 if sex == "Male" else 0

# Conversion rate (example: 1 USD = 83 INR)
usd_to_inr = 83

# Predict button
if st.button("Predict"):
    with st.spinner("Analyzing inputs..."):
        time.sleep(2)  # Simulate processing time
    
    # Prepare the input for the model
    features = np.array([[age, bmi, children, smoker, region, sex]])
    
    # Make prediction
    pred = model.predict(features)[0] * usd_to_inr
    
    # Display result with animation effect
    if pred < 0:
        st.error("Error calculating amount!")
    else:
        st.markdown(f"<h2 class='heartbeat-text'>Expected medical cost is ₹{pred:.2f}</h2>", unsafe_allow_html=True)
