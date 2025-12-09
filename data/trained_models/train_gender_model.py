import os                                           # For file and folder operations
import cv2                                          # For image reading and resizing
import numpy as np                                  # For numerical operations
from tensorflow.keras.applications import EfficientNetB0   # Pretrained EfficientNet model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D  # Model layers
from tensorflow.keras.models import Sequential       # Sequential model builder
from sklearn.model_selection import train_test_split  # For splitting dataset

# Function to load dataset
def load_data():

    images = []                                     # Store image data
    genders = []                                    # Store gender labels
    dataset_path = "../data/UTKFace"               # Dataset folder path

    # Loop through all files in dataset folder
    for filename in os.listdir(dataset_path):

        # Process only image files
        if filename.endswith(".jpg"):

            # Extract gender label from filename
            gender = int(filename.split("_")[1])

            # Read image from disk
            img = cv2.imread(os.path.join(dataset_path, filename))

            # Resize image for EfficientNet input size
            img = cv2.resize(img, (224, 224))

            # Normalize pixel values between 0 and 1
            img = img / 255.0

            # Store processed image
            images.append(img)

            # Store corresponding gender label
            genders.append(gender)

    # Convert lists into NumPy arrays
    return np.array(images), np.array(genders)

# Load dataset
X, y = load_data()

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build the model using Sequential API
model = Sequential([

    # Load EfficientNetB0 as feature extractor
    EfficientNetB0(
        weights='imagenet', 
        include_top=False, 
        input_shape=(224, 224, 3)
    ),

    # Convert feature maps to single vector
    GlobalAveragePooling2D(),

    # Fully connected hidden layer
    Dense(128, activation='relu'),

    # Output layer for binary classification (male/female)
    Dense(1, activation='sigmoid')
])

# Compile the model with optimizer, loss, and metrics
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model on training data
model.fit(
    X_train, 
    y_train, 
    epochs=10, 
    validation_data=(X_test, y_test)
)

# Save the trained model to disk
model.save("../data/trained_models/gender_model.h5")

# Print confirmation message
print("Model saved to data/trained_models/gender_model.h5!")
