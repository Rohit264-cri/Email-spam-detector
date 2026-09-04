import streamlit as st
import joblib
from xgboost import XGBClassifier


vectorizer = joblib.load("vectorizer.joblib")
model = XGBClassifier()
model.load_model("spam_model.json")

st.title("📧 Spam  Email Detector Web App")

user_input = st.text_area("Enter email:")

if st.button("Predict"):
    X = vectorizer.transform([user_input])
    prediction = model.predict(X)[0]
    
    if prediction == 1:
        st.error("🚨 This looks like SPAM!")
    else:
        st.success("✅ This looks SAFE!")
