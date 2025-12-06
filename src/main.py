# src/main.py
import cv2
from src.utils import get_location  # Changed
from src.gender_detection import detect_gender  # Changed
from src.gesture_recognition import detect_sos  # Changed
from src.anomaly_detection import detect_anomaly  # Changed
from src.alerts import send_sms  # Changed

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Check for SOS gesture
    if detect_sos(frame):
        lat, lon = get_location()
        send_sms(lat, lon)
        print("SOS Detected!")
    
    # Check for lone woman anomaly
    if detect_anomaly(frame):
        print("Lone woman detected at night!")
    
    # Display live feed
    cv2.imshow('Women Safety System', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()