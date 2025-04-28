import os
import pickle
from tensorflow.keras.models import load_model  # type: ignore
from app.config import DENSENET_MODEL_PATH, MOBILENET_MODEL_PATH, CNN_MODEL_PATH, LABEL_ENCODER_PATH

# Mapping model keys to their paths
MODEL_PATHS = {
    "D": DENSENET_MODEL_PATH,
    "M": MOBILENET_MODEL_PATH,
    "C": CNN_MODEL_PATH
}

def load_model_by_key(model_key: str):
    """
    Load the deep learning model and class labels based on the provided key.

    Args:
        model_key (str): Key identifying which model to load ('D', 'M', or 'C').

    Returns:
        model: Loaded Keras model.
        class_labels: Loaded class labels.
    """
    # Ensure the model key is uppercase
    model_key = model_key.upper()

    # Validate the model key
    if model_key not in MODEL_PATHS:
        raise ValueError(f"Invalid model key '{model_key}'. Choose from: {list(MODEL_PATHS.keys())}")

    model_path = MODEL_PATHS[model_key]

    # Load the selected model
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    model = load_model(model_path)

    # Load class labels
    if not os.path.exists(LABEL_ENCODER_PATH):
        raise FileNotFoundError(f"Label encoder file not found at {LABEL_ENCODER_PATH}")

    with open(LABEL_ENCODER_PATH, "rb") as f:
        class_labels = pickle.load(f)

    return model, class_labels
