import pickle
import os

def load_model():
    with open("path/to/your_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def suggest_activity(user_input):
    model = load_model()
    suggestion = model.predict([user_input])  # Replace with actual prediction logic
    return suggestion
