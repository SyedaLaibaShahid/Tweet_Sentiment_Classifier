# 📘 Tweet Sentiment Classifier (Streamlit App)

This project is a Machine Learning–based Tweet Sentiment Classifier deployed using Streamlit Cloud.
It takes a tweet as input and predicts its sentiment using a trained ML model.


## ▶️ How to Run Locally
### 1. Clone the repo
git clone https://github.com/your-username/tweet-sentiment-classifier.git
cd tweet-sentiment-classifier
### 2. Install dependencies
pip install -r requirements.txt
### 3. Run the app
streamlit run app.py


## 🧪 Model Prediction Flow
User enters a tweet, 
Text → vectorized using TF-IDF, 
Model predicts sentiment, 
Result is displayed on the app interface


## 🎨 Streamlit UI Features
Clean text input box, 
Predict button, 
Sentiment output, 
Real-time inference


## 👩‍💻 Technologies Used
Python, 
Scikit-learn, 
Pandas / NumPy, 
Streamlit, 
Joblib, 
TfidfVectorizer