import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from fer import FER
from PIL import Image
import numpy as np
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # ✅ store in environment variable
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set in environment variables")
genai.configure(api_key=GEMINI_API_KEY)

@app.route("/detect-emotion", methods=["POST"])
def detect_emotion():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    try:
        # Load image safely
        image = Image.open(file.stream).convert("RGB")  # ✅ force RGB
        image_np = np.array(image)

        # Check shape
        if len(image_np.shape) != 3 or image_np.shape[2] != 3:
            return jsonify({"error": "Invalid image format. Please upload a color image."}), 400

        # Detect emotionpip install flask flask-cors fer pillow numpy google-generativeai

        detector = FER()
        emotions = detector.detect_emotions(image_np)

        if not emotions:
            return jsonify({"error": "No face detected"}), 400

        dominant_emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)

        # Gemini prompt
        model = genai.GenerativeModel("gemini-1.5-flash")
        if dominant_emotion.lower() == "happy":
            prompt = "Give me an uplifting, positive quote for the day."
        else:
            prompt = f"Someone is feeling {dominant_emotion}. Give a kind and encouraging message to make them feel better."

        response = model.generate_content(prompt)

        return jsonify({
            "emotion": dominant_emotion,
            "message": response.text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
