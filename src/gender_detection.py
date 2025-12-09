# src/gender_detection.py
# ---------------------------------------------------------
# GENDER DETECTION MODULE
# ---------------------------------------------------------
# This file is responsible for detecting the gender of a
# person using a trained deep learning model.
#
# Workflow:
# 1. A face image is received as input
# 2. The face is resized and normalized
# 3. The trained model predicts gender
# 4. Output is returned as "female" or "male"
# ---------------------------------------------------------

import cv2
from tensorflow.keras.models import load_model
import numpy as np

# ---------------------------------------------------------
# Load the pre-trained gender detection model
# This model is trained beforehand and stored in the
# "data/trained_models" directory.
# ---------------------------------------------------------
model = load_model('data/trained_models/gender_model.h5')  # Update path if needed

def detect_gender(face_roi):
    """
    This function predicts the gender of a person
    based on the face region extracted from the image.

    Parameters:
        face_roi (numpy array): Cropped face image

    Returns:
        "female" if the predicted probability is greater than 0.5
        "male" otherwise
    """
    
    # Resize the face image to match model input size
    resized = cv2.resize(face_roi, (128, 128))

    # Normalize pixel values between 0 and 1
    normalized = resized / 255.0

    # Expand dimensions to match model input shape
    prediction = model.predict(np.expand_dims(normalized, axis=0))

    # Return gender prediction based on threshold
    return "female" if prediction[0][0] > 0.5 else "male"
