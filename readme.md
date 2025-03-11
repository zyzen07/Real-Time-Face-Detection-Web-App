Real-Time Face Detection with Emotion Analysis

This project is a Real-Time Face Detection System with Emotion Analysis built using HTML, CSS, JavaScript, Python (Flask), and MySQL. The system detects faces in real-time, predicts emotions, and provides suggestions based on the detected emotion.

The primary goal of this project is to assist users in tracking their emotional state and provide helpful suggestions for improved mental well-being. By combining computer vision and web technologies, this solution offers a seamless experience for users to engage with their emotional state in real-time.

🚀 Features

✅ Real-time face detection using OpenCV✅ Emotion recognition with actionable suggestions✅ User-friendly interface for live tracking✅ Integration with MySQL for data storage✅ Flask-based web application for smooth performance

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python (Flask)

Database: MySQL Workbench

Computer Vision: OpenCV for face detection

📷 Demo Image go to demo images foler 


Sample image showcasing the system in action:



⚙️ Installation & Setup

Clone the Repository:

git clone https://github.com/zyzen07/Real-Time-Face-Detection-Web-App.git
cd realtime-face-detection

Install Dependencies:

pip install flask opencv-python

Set Up MySQL Database:

Create a database in MySQL Workbench

Import the required .sql file (if available)

Run the Application:

python app.py

Access the App:Navigate to http://127.0.0.1:5000/ in your browser.

📂 Project Structure

/your_project_folder
├── templates
│   ├── index.html
│   └── live_track.html
├── static
│   ├── style.css
├── model
│   └── model.pkl
├── app.py
├── demo_image.png
└── README.md

🧠 How It Works

The user accesses the Mental Health Tracker homepage.

Clicking "Live Track" starts the live video feed.

The system detects faces in real-time and predicts the user's emotion (e.g., happy, neutral, sad).

A suitable suggestion is provided based on the detected emotion.

🐞 Troubleshooting

If the camera feed does not load, ensure that your webcam is properly connected.

For port conflicts, change the port in app.py (e.g., app.run(port=5001)).

📧 Contact

For any questions or contributions, feel free to reach out! 😊

E-mail : selvavishnug@gmail.com
linked in: https://www.linkedin.com/in/selvavishnug