#Emotion Detector - 😊 AI-Powered Emotion Recognition

A web application that uses **Machine Learning** to analyze any image and predict its overall emotion (e.g., Happy, Sad, Angry, Neutral, etc). Built with **React.js** and **Flask**, it processes uploaded images and uses **Google Gemini API** to generate meaningful one-line descriptions based on the detected emotion.

🌟 Features

- ✅ **Image-Based Detection** – Works with any image, not just faces.  
- 🎯 **Multi-Emotion Recognition** – Supports emotions like Happy, Sad, Angry, Neutral, Surprise, etc.  
- 🧠 **AI-Powered Descriptions** – Uses Google Gemini API to give one-line emotion summaries.  
- ⚡ **Fast & Accurate** – Uses a trained deep learning model for predictions.  
- 📱 **User-Friendly UI** – Clean and responsive design.
---

**🛠️ Tech Stack**

**Frontend:**
- React.js
- JavaScript (ES6+)
- Axios
- Google Fonts
- CSS-in-JS (inline styles + animations)

**Backend:**
- Python (Flask)
- FER (Facial Emotion Recognition)
- Pillow
- NumPy
- Google Gemini API
- Flask-CORS

**Other Tools:**
- Git & GitHub
- Localhost API for development

---

## ⚙ How It Works

1. User uploads an image.  
2. Image is sent to the **Flask backend** in Python.  
3. The trained model processes the image and predicts its emotion.  
4. **Google Gemini API** generates a one-line description based on the detected emotion.  
5. Result (emotion + description) is sent back and displayed on the **frontend**.

---
## ⚙ How It Works / Running the App

```bash
Step 1: Clone the Repository
git clone <your-repo-url>
cd emotion-detector

Step 2: Run Backend
cd emotion-backend
python -m venv venv          # Create a virtual environment (if not already created)
venv\Scripts\activate        # Activate the virtual environment (Windows)
# For Mac/Linux use: source venv/bin/activate
pip install -r requirements.txt
python app.py                # Start the Flask backend server

Step 3: Run Frontend (React)
cd emotion-frontend
npm install                  # Install frontend dependencies
npm start                    # Start the React development server

Step 4: Use the App
Open your browser at http://localhost:3000
Upload an image to detect emotion
See the predicted emotion along with the AI-generated description
```

---

📸 Screenshots

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ca0a9de8-9a1a-4666-8465-b881c0b8919e" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/43977dfe-11fe-4c19-9251-71d46b5176b7" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/4bbed2f1-cc41-4307-993e-ae0ffeca09bd" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/bd24780c-b62d-43e2-8a7c-d5ae5c7d0ae0" />

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/47def79d-6ff7-4cd9-9b23-164be9f9675a" />

---

## 📌 Future Improvements

- 📊 Improve model accuracy with larger, more diverse datasets.  
- 👥 Support multiple emotions in a single image.  
- 🌍 Deploy the app for public use.

---

## 👤 Author

**Tejas Nagpure**  
[GitHub](https://github.com/TejSync) |  [LinkedIn](https://www.linkedin.com/in/tejas-nagpure-0598a8267/)
