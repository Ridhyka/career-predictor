import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (Assuming a CSV file named 'career_data.csv')
# df = pd.read_csv("cs_students.csv")
df = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\careeer\cs_students.csv")


print(df.head())
print("Unique Interested Domains:", df["Interested Domain"].unique())
df.drop(columns=['Student ID', 'Name','Major'], inplace=True)
label_encoders = {}  # Store encoders for later use


for col in ["Gender", "Future Career", "Python", "SQL", "Java"]:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

# 🔹 One-Hot Encoding for Unordered Categorical Features
df = pd.get_dummies(df, columns=["Interested Domain", "Projects"], drop_first=True)

print(df.head())
# 🔹 Separate Features (X) and Target Variable (y)
X = df.drop("Future Career", axis=1)
y = df["Future Career"]

# 🔹 Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 🔹 Scale Numerical Features

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# 🔹 Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 🔹 Evaluate the Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
 # 🔹 Save Model & Scaler for Future Use
joblib.dump(model, "career_prediction_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")  # Save encoders for decoding predictions

print("Model, scaler, and encoders saved successfully!")

