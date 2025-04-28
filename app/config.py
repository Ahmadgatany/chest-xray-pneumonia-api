import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Saved models path
MODEL_DIR = os.path.join(BASE_DIR, "saved_models")

# Specific model files
CNN_MODEL_PATH = os.path.join(MODEL_DIR, "cnn_model.h5")
MOBILENET_MODEL_PATH = os.path.join(MODEL_DIR, "mobilenetv2_model.h5")
DENSENET_MODEL_PATH = os.path.join(MODEL_DIR, "densenet121_model.h5")
LABEL_ENCODER_PATH = os.path.join(MODEL_DIR, "class_labels.pkl")

# Allowed image extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

# Default model key
DEFAULT_MODEL_KEY = "D"  # This can be the default model key, e.g., "D" for DenseNet

# API settings
API_TITLE = "Chest X-ray Pneumonia Classifier API"
API_VERSION = "1.0.0"

# Image input size for models (you can adjust based on your models)
IMAGE_HEIGHT = 150
IMAGE_WIDTH = 150
