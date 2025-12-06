# src/gender_detection.py
import cv2
from tensorflow.keras.models import load_model
import numpy as np

# Load your trained gender model
model = load_model('data/trained_models/gender_model.h5')  # Update path if needed

def detect_gender(face_roi):
    # Preprocess face ROI for your model (example)
    resized = cv2.resize(face_roi, (128, 128))
    normalized = resized / 255.0
    prediction = model.predict(np.expand_dims(normalized, axis=0))
    return "female" if prediction[0][0] > 0.5 else "male"