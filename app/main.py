from fastapi import FastAPI
from app.routes import predict
from app.config import API_TITLE, API_VERSION

# Create FastAPI app with settings from config.py
app = FastAPI(
    title=API_TITLE,
    description="Deep learning powered API to classify pneumonia from chest X-ray images.",
    version=API_VERSION
)

# Include the prediction API router
app.include_router(predict.router)

# Root route to confirm the API is running
@app.get("/")
async def root():
    return {"message": f"{API_TITLE} is running!"}
