# src/main.py

import cv2                                   # For webcam and frame processing
from src.utils import get_location            # Get user's location (lat, lon)
from src.gender_detection import detect_gender  # Gender detection module
from src.gesture_recognition import detect_sos  # Detect SOS hand gesture
from src.anomaly_detection import detect_anomaly  # Detect unsafe situations
from src.alerts import send_sms               # Send emergency SMS alert

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()                   # Read a frame from webcam
    if not ret:
        break                                 # Stop if frame not captured
    
    # Check for SOS gesture
    if detect_sos(frame):                     
        lat, lon = get_location()             # Get user location
        send_sms(lat, lon)                    # Send SMS alert
        print("SOS Detected!")
    
    # Check for lone woman anomaly
    if detect_anomaly(frame):                 
        print("Lone woman detected at night!")
    
    # Display live feed
    cv2.imshow('Women Safety System', frame)   # Show webcam window
    if cv2.waitKey(1) & 0xFF == ord('q'):      # Quit when 'q' pressed
        break

cap.release()                                  # Release webcam
cv2.destroyAllWindows()                        # Close all windows
