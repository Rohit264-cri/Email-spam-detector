# 📧 Email Spam Detector

A Machine Learning web application that classifies emails as **Spam** or **Not Spam** in real-time using an **XGBoost Classifier** and **CountVectorizer**, deployed with **Streamlit**.



## 📌 Overview

Spam emails are a common problem in everyday communication. This project uses Machine Learning to automatically detect whether an email is spam or legitimate, based on its text content.

The model was trained on a labeled email dataset and achieves **98.69% accuracy** on unseen test data.



## 🧠 Tech Stack

| Category | Tools/Libraries |
|       ---|              ---|
| Language | Python |
| ML Model | XGBoost Classifier |
| Text Vectorization | CountVectorizer (Scikit-learn) |
| Web Framework | Streamlit |
| Model Serialization | Joblib |
| Data Handling | Pandas, NumPy |


## 📊 Model Performance

- **Test Accuracy:** 98.69%
- **Cross-Validation Mean Accuracy (5-fold):** 97.8%
- **Confusion Matrix:**

|  | Predicted: Not Spam | Predicted: Spam |
|---|---|---|
| **Actual: Not Spam** | 846 | 10 |
| **Actual: Spam**     | 5  | 285 |

The model shows consistent performance across all cross-validation folds, indicating low overfitting and strong generalization.


## ⚙️ How It Works

1. Raw email text is cleaned and converted into numerical features using **CountVectorizer**.
2. The vectorized data is fed into a trained **XGBoost Classifier**.
3. The model predicts whether the email is spam (`1`) or not spam (`0`).
4. Results are displayed instantly through a simple **Streamlit** web interface.



## 📂 Project Structure

spam-detector-app/
├── app.py                 # Streamlit web application
├── spam_model.joblib       # Trained XGBoost model
├── vectorizer.joblib        # Fitted CountVectorizer
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation


## 📦 Requirements

streamlit
scikit-learn
xgboost
joblib
pandas
numpy


## 🖥️ Usage

1. Paste or type the email text into the input box.
2. Click the **predict** button.
3. The app will instantly display whether the email is **Spam** or **Not Spam**.


## 🔮 Future Improvements

- Add prediction confidence/probability score
- Support for uploading `.txt` or `.eml` email files
- Try advanced NLP techniques (TF-IDF, word embeddings)
- Add a dark mode / improved UI
- Deploy with a custom domain


## 🙌 Acknowledgements

Built as a hands-on project to understand the complete Machine Learning lifecycle — from data preprocessing and model training to deployment as a real-world web application.

---

## 📬 Contact

Feel free to connect or reach out for feedback and suggestions!

**Rohit**


⭐ If you found this project useful, consider giving it a star on GitHub!
