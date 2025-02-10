# Career Predictor 🎯  

![Python](https://img.shields.io/badge/Python-3.8+-blue)  
![Flask](https://img.shields.io/badge/Flask-3.1.0-green)  
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Sklearn-red)  

A machine learning-powered career prediction web app that helps users determine potential career paths based on their skills, interests, and academic performance.  

🔗 **Live Demo**: [Career Predictor](https://career-predictor.up.railway.app/)  

## 🚀 Features  
- Predicts a career path based on input data (GPA, skills, domain, projects, etc.).  
- Built using Flask as the backend.  
- Utilizes a trained machine learning model for prediction.  
- Responsive and user-friendly UI.  

## 🧠 Machine Learning Model  
The app uses a **Logistic Regression** trained on a dataset containing various student profiles, including GPA, programming skills (Python, Java, SQL), and preferred domains. The model predicts the most suitable career path based on this information.  

- **Libraries Used**:  
  - `scikit-learn` for model training  
  - `pandas` and `numpy` for data processing  
  - `joblib` for model serialization  

The trained model is loaded in Flask and used to provide predictions based on user input.  

## 🖥️ Screenshot  
<img src="/static/Screenshot (20).png" alt="Career Predictor Web App" width="800" height="500">  

## 🛠 Installation  
1. Clone this repository:  
   ```sh
   git clone https://github.com/Ridhyka/career-predictor.git
   cd career-predictor

## 🚀 Deployment  
The app is deployed on **Railway**. You can access it here:  
🔗 [Career Predictor](https://career-predictor.up.railway.app/)  

## 📜 License  
This project is open-source and available under the **MIT License**.  


