from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # No rate limiting
    # No authentication
    prompt = request.json["prompt"]
    return jsonify({"output": f"Prediction for {prompt}"})

API_KEY = "123456"  # Hardcoded credential
