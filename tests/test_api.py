import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from pathlib import Path


# Create a TestClient instance for our FastAPI app
client = TestClient(app)

# Path to a sample image for testing
SAMPLE_IMAGE_PATH = Path("tests/test_image1.jpeg")

# Test if the /predict/ endpoint returns 200 OK and valid response
def test_predict_endpoint_success():
    # Check if sample image exists
    assert SAMPLE_IMAGE_PATH.exists(), "Sample image not found."

    # Open the sample image in binary mode
    with open(SAMPLE_IMAGE_PATH, "rb") as image_file:
        # Send POST request to the /predict/ endpoint
        response = client.post(
            "/predict/?model_name=D",  # You can test with "C" or "M" also
            files={"file": ("sample_image.jpeg", image_file, "image/jpeg")}
        )
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200

    # Parse the JSON response
    result = response.json()

    # Assert that the expected keys exist in the response
    assert "predicted_class" in result
    assert "confidence" in result
    assert "model_used" in result

    # Optional: Additional checks
    assert result["model_used"] == "D"
    assert 0.0 <= result["confidence"] <= 1.0

# Test if sending an invalid model name returns 400 error
def test_predict_invalid_model_key():
    with open(SAMPLE_IMAGE_PATH, "rb") as image_file:
        response = client.post(
            "/predict/?model_name=INVALID",
            files={"file": ("sample_image.jpeg", image_file, "image/jpeg")}
        )
    
    # Assert that the response status code is 400 Bad Request
    assert response.status_code == 400

    # Optional: check error message content
    result = response.json()
    assert "detail" in result
    assert "Invalid model key" in result["detail"]
