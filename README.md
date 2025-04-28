# chest-xray-pneumonia-api

This project is a **FastAPI**-based REST API for diagnosing pneumonia from chest X-ray images using deep learning models.

## Project Structure

```bash
chest-xray-pneumonia-api/
├── app/
│   ├── config.py
│   ├── main.py
│   ├── loaders/
│   │   └── model_loader.py
│   ├── routes/
│   │   └── predict.py
│   └── utils/
│       └── preprocessing.py
├── notebooks/
│   └── chest-x-ray-pneumonia-classifier-cnn-tl.ipynb
├── saved_models/
│   ├── class_labels.pkl
│   ├── cnn_model.h5
│   ├── densenet121_model.h5
│   └── mobilenetv2_model.h5
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_image1.jpeg
├── azure_deploy.md
├── Dockerfile
├── README.md
├── requirements.txt
```

## Features

- Upload chest X-ray images to predict if the image indicates pneumonia.
- Pretrained models used: **CNN**, **DenseNet121**, **MobileNetV2**.
- REST API built with **FastAPI**.
- Dockerfile included for containerization.
- Unit tests provided using **pytest**.

## Dataset

The dataset used to train and evaluate the models can be found here:  
👉 [Chest X-Ray Images (Pneumonia) - Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/chest-xray-pneumonia-api.git
   cd chest-xray-pneumonia-api
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Usage

- Navigate to:
  ```
  http://127.0.0.1:8000/docs
  ```
- Upload a chest X-ray image and get a prediction through the interactive Swagger UI.

---

## Docker Support

To build and run the project using Docker:

```bash
docker build -t chest-xray-pneumonia-api .
docker run -d -p 8000:8000 chest-xray-pneumonia-api
```

Then open your browser at:
```
http://localhost:8000/docs
```

---

## Azure Deployment

See the full guide here:  
👉 [azure_deploy.md](./azure_deploy.md)

---

## Testing

Run tests using **pytest**:

```bash
pytest tests/
```

---

## License

This project is licensed under the MIT License.
