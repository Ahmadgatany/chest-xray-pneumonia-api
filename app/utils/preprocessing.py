from PIL import Image
import numpy as np
import io
from app.config import IMAGE_HEIGHT, IMAGE_WIDTH  

def preprocess_image(image_bytes: bytes):
    # Open image from bytes
    image = Image.open(io.BytesIO(image_bytes))
    
    # Ensure the image is in RGB format (3 channels)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize the image to match the model input size from config.py
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))  # Use values from config.py
    
    # Convert to numpy array
    image_array = np.array(image)
    
    # Normalize the image to [0, 1] range
    image_array = image_array / 255.0  # Normalize to [0, 1]
    
    # Expand dims to match model input (1, height, width, channels)
    image_array = np.expand_dims(image_array, axis=0)
    
    # Optional: log the image shape to verify dimensions
    print(f"Processed image shape: {image_array.shape}")
    
    return image_array
