from flask import Flask, request, jsonify
import os  # Import Flask and tools for handling data

app = Flask(__name__)  # Create Flask app

@app.route("/")  
def home():
    return "Flask API is running!"

# New API route that takes JSON data and returns a response
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get JSON data sent by the user
    input_value = data.get("input", 0)  # Get "input" key from JSON, default to 0 if missing
    
    # Example: Just multiply the input by 2 (you'll replace this with your AI model later)
    result = input_value * 2  
    
    return jsonify({"prediction": result})  # Send the result back as JSON

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)