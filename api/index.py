



from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model, scaler, and encoders
model = joblib.load("career_prediction_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Get the feature names used during training
expected_columns = scaler.feature_names_in_
df = pd.read_csv("cs_students.csv")  # Make sure the path is correct
unique_domains = df["Interested Domain"].unique()
projects = df["Projects"].unique()

@app.route("/")
def home():
    return render_template("index.html", domains=unique_domains, projects=projects)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Received Data:", data)  # Debugging

        # Create a dictionary with default values of 0 for missing features
        input_data = {col: 0 for col in expected_columns}

        # Convert numerical values
        input_data["Age"] = float(data["age"])
        input_data["GPA"] = float(data["gpa"])

        # Encode categorical values using label encoders
        input_data["Gender"] = label_encoders["Gender"].transform([data["gender"]])[0]
        input_data["Python"] = label_encoders["Python"].transform([data["python"]])[0]
        input_data["SQL"] = label_encoders["SQL"].transform([data["sql"]])[0]
        input_data["Java"] = label_encoders["Java"].transform([data["java"]])[0]

        # One-hot encode Interested Domain and Projects dynamically
        domain_column = f"Interested Domain_{data['domain']}"
        projects_column = f"Projects_{data['projects']}"

        if domain_column in input_data:
            input_data[domain_column] = 1
        if projects_column in input_data:
            input_data[projects_column] = 1

        # Convert input dictionary to DataFrame
        input_df = pd.DataFrame([input_data])

        # Scale the input data
        input_scaled = scaler.transform(input_df)

        # Predict the career
        prediction = model.predict(input_scaled)
        predicted_career = label_encoders["Future Career"].inverse_transform(prediction)[0]

        return jsonify({"prediction": predicted_career})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
