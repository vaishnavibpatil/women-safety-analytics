# Women Safety Analytics System

This project is a real-time computer vision-based safety system that detects SOS hand gestures, identifies gender using a deep learning model, detects unsafe situations such as a lone woman at night, and sends instant emergency SMS alerts with live location using the Twilio API.
The system continuously monitors webcam video, analyzes each frame for danger signals, and automatically triggers alerts without requiring manual input from the user.

# Features

Real-time SOS hand gesture detection
Gender detection using deep learning
Lone woman anomaly detection at night
Live location tracking using IP-based API
Automatic emergency SMS alerts using Twilio
Continuous webcam monitoring

# Technologies Used

Python
OpenCV
MediaPipe
TensorFlow / Keras
EfficientNetB0
Scikit-learn
Twilio API

# How It Works

The webcam captures live video.
SOS gestures and anomalies are detected from each frame.
User location is fetched automatically.
Emergency SMS with live location is sent to the registered contact.
