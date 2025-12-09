# anomaly_detection.py
# ---------------------------------------------------------
# ANOMALY DETECTION MODULE
# ---------------------------------------------------------
# This file is responsible for detecting unsafe situations
# from the video feed. One example anomaly implemented here
# is detecting a "lone woman at night".
#
# The logic:
# 1. Detect faces in the video frame
# 2. Detect gender of each face
# 3. Count number of women
# 4. If exactly one woman is detected at night, raise an alert
# ---------------------------------------------------------

import cv2
import time
from gender_detection import detect_gender  # Used to detect gender from a face image

def detect_anomaly(frame, timestamp):
    """
    This function detects unsafe situations (anomalies) from a video frame.

    Parameters:
        frame (numpy array): Current video frame captured from webcam
        timestamp (float): Current time used to determine night condition

    Returns:
        "lone_woman_alert" if unsafe condition is detected
        None if no anomaly is detected
    """

    # ---------------------------------------------------------
    # FACE DETECTION
    # ---------------------------------------------------------
    # Using Haar Cascade Classifier to detect faces in the frame
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # Convert frame to grayscale (Haar works on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # ---------------------------------------------------------
    # GENDER COUNTING
    # ---------------------------------------------------------
    # Count how many women are present in the frame
    women_count = 0

    for (x, y, w, h) in faces:
        # Extract face region from the frame
        face_roi = frame[y:y+h, x:x+w]

        # Detect gender of the extracted face
        gender = detect_gender(face_roi)

        # If detected gender is female, increase the counter
        if gender == 'female':
            women_count += 1

    # ---------------------------------------------------------
    # ANOMALY DETECTION LOGIC
    # ---------------------------------------------------------
    # Condition:
    # If only one woman is detected AND it is night time,
    # then raise a "lone_woman_alert"
    
    if women_count == 1 and is_night(timestamp):
        return "lone_woman_alert"

    # If no abnormal condition is detected, return None
    return None
