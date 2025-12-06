import os
import cv2
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split

# Function to load dataset
def load_data():
    images = []
    genders = []
    dataset_path = "../data/UTKFace"  # Adjust this path if needed

    for filename in os.listdir(dataset_path):
        if filename.endswith(".jpg"):
            gender = int(filename.split("_")[1])  # Extract gender from filename
            img = cv2.imread(os.path.join(dataset_path, filename))
            img = cv2.resize(img, (224, 224))  # Resize for EfficientNetB0
            img = img / 255.0  # Normalize pixel values
            images.append(img)
            genders.append(gender)

    return np.array(images), np.array(genders)

# Load data
X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the model using Sequential
model = Sequential([
    EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3)),
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification (male/female)
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save the trained model
model.save("../data/trained_models/gender_model.h5")
print("Model saved to data/trained_models/gender_model.h5!")