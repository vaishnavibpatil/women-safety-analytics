# src/gesture_recognition.py
import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose

def detect_sos(frame):
    with mp_pose.Pose(min_detection_confidence=0.5) as pose:
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            # Example: Check if both hands are above head
            left_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
            right_wrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
            if left_wrist.y < 0.2 and right_wrist.y < 0.2:  # Adjust threshold as needed
                return True
        return False