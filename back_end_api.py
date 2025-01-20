from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("intrusion_detection_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the input data
    data = request.json
    input_data = pd.DataFrame([data])

    # Make a prediction
    prediction = model.predict(input_data)
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)