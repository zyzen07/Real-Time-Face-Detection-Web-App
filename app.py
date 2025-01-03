from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load your model (ensure the path is correct)
def load_model():
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Dummy function for facial expression analysis
def analyze_face_expression(image):
    # For demo purposes, let's return a random emotion
    emotions = ['happy', 'neutral', 'sad']
    return np.random.choice(emotions)

# Suggest activities based on user response
def suggest_activity(emotion):
    if emotion == 'happy':
        return "Great to see you happy! Keep it up by doing something you enjoy."
    elif emotion == 'neutral':
        return "You're feeling neutral. How about taking a short walk?"
    else:
        return "It seems you might need some positivity. Try some deep breathing exercises."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_suggestion', methods=['POST'])
def get_suggestion():
    user_response = request.form['response']
    suggestion = suggest_activity(user_response)
    return jsonify({'suggestion': suggestion})

@app.route('/live_track', methods=['GET'])
def live_track():
    return render_template('live_track.html')

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    # Get the image data from the client
    image_data = request.form['image']
    # Process the image data
    nparr = np.fromstring(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Analyze the face expression
    emotion = analyze_face_expression(img)
    suggestion = suggest_activity(emotion)
    
    return jsonify({'emotion': emotion, 'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)
