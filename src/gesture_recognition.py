# src/gesture_recognition.py

import cv2                       # OpenCV for image processing
import mediapipe as mp           # MediaPipe for pose detection
import numpy as np               # NumPy for numerical operations

mp_pose = mp.solutions.pose     # Load MediaPipe pose solution

def detect_sos(frame):

    # Initialize pose detection model
    with mp_pose.Pose(min_detection_confidence=0.5) as pose:

        # Convert frame from BGR to RGB
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # If body landmarks are detected
        if results.pose_landmarks:

            # Get left wrist position
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]

            # Get right wrist position
            right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]

            # Check if both hands are raised above head
            if left_wrist.y < 0.2 and right_wrist.y < 0.2:  # Threshold for raised hands
                return True     # SOS gesture detected

        return False            # No SOS gesture detected
