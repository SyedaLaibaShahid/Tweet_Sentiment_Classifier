import streamlit as st
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Tweet Sentiment Classifier")
st.write("Enter a tweet below and the model will classify it.")

user_text = st.text_area("Tweet:", "")

if st.button("Predict"):
    if user_text.strip() == "":
        st.warning("Please enter a tweet.")
    else:
        X = vectorizer.transform([user_text])
        pred = model.predict(X)[0]

        if pred == 0:
            label = "Negative"
        elif pred == 1:
            label = "Positive"
        else:
            label = str(pred)

        st.success(f"Prediction: **{label}**")
