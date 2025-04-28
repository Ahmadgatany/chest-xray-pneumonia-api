from fastapi import APIRouter, File, UploadFile, HTTPException, Query
from app.loaders.model_loader import load_model_by_key
from app.utils.preprocessing import preprocess_image
from app.config import ALLOWED_EXTENSIONS, DEFAULT_MODEL_KEY
import numpy as np
import os

router = APIRouter()

def allowed_file(filename: str) -> bool:
    """
    Check if the uploaded file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@router.post("/predict/")
async def predict(
    file: UploadFile = File(...),
    model_name: str = Query(DEFAULT_MODEL_KEY, description="Model key: D, M, or C")  # default is "D"
):
    try:
        # Check if file has an allowed extension
        if not allowed_file(file.filename):
            raise HTTPException(status_code=400, detail="Invalid file extension. Allowed extensions are: png, jpg, jpeg.")
        
        print(f"Received file: {file.filename}")
        print(f"Using model: {model_name}")

        # Load the selected model and class labels
        model, class_labels = load_model_by_key(model_name)

        # Read uploaded image file
        contents = await file.read()

        # Preprocess image for model prediction
        image = preprocess_image(contents)

        # Perform prediction
        prediction = model.predict(image)
        # predicted_class = class_labels[np.argmax(prediction)]
        # For binary classification
        predicted_index = 1 if prediction[0][0] > 0.5 else 0
        predicted_class = class_labels[predicted_index]

        return {
            "predicted_class": predicted_class,
            "confidence": float(np.max(prediction)),
            "model_used": model_name.upper()
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
