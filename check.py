import pandas as pd
import numpy as np
import joblib

# Load the trained model and encoders
model = joblib.load("career_prediction_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# 🔹 Load dataset again to get correct column names
df = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\careeer\cs_students.csv")
df.drop(columns=['Student ID', 'Name', 'Major'], inplace=True)

# Apply Label Encoding (same as training data)
for col in ["Gender", "Future Career", "Python", "SQL", "Java"]:
    df[col] = label_encoders[col].transform(df[col])

# Apply One-Hot Encoding (same as training)
df = pd.get_dummies(df, columns=["Interested Domain", "Projects"], drop_first=True)

# 🔹 Get correct feature names from trained dataset
feature_columns = df.drop("Future Career", axis=1).columns.tolist()

# 🔹 Define new student details
new_student_data = {
    "Age": 27,
    "GPA": 2.5,
    "Gender": label_encoders["Gender"].transform(["Female"])[0],  
    "Python": label_encoders["Python"].transform(["Strong"])[0],  
    "SQL": label_encoders["SQL"].transform(["Strong"])[0],
    "Java": label_encoders["Java"].transform(["Strong"])[0],
}

# 🔹 Add missing one-hot encoded columns (Set default 0)
for col in feature_columns:
    new_student_data[col] = new_student_data.get(col, 1)

# Convert to DataFrame
new_student_df = pd.DataFrame([new_student_data])

# Ensure column order matches training data
new_student_df = new_student_df[feature_columns]

# 🔹 Apply Scaling
new_student_scaled = scaler.transform(new_student_df)

# 🔹 Predict Career
predicted_career = model.predict(new_student_scaled)

# 🔹 Decode the prediction
predicted_career_label = label_encoders["Future Career"].inverse_transform(predicted_career)

print("Predicted Career:", predicted_career_label[0])

if "Interested Domain" in label_encoders:
    print("Unique Interested Domains:", list(label_encoders["Interested Domain"].classes_))
else:
    print("Error: 'Interested Domain' not found in label encoders.")