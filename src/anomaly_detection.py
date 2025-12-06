# anomaly_detection.py
import cv2
import time
from gender_detection import detect_gender  # Absolute import

def detect_anomaly(frame, timestamp):
    # Detect people (using YOLO or Haar cascades)
    # Example: Use Haar cascade for simplicity
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Count women and men
    women_count = 0
    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        gender = detect_gender(face_roi)
        if gender == 'female':
            women_count += 1

    # Anomaly: Lone woman at night (timestamp-based logic)
    if women_count == 1 and is_night(timestamp):
        return "lone_woman_alert"
    return None