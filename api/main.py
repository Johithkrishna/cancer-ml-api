from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class Features(BaseModel):
    features: list[float]

print("🚀 Starting API...")

@app.get("/")
def home():
    return {"message": "Cancer Prediction API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def get_prediction(data: Features):
    if len(data.features) != 30:
        return {"error": "Exactly 30 features required"}

    result = predict(data.features)

    label = "Malignant" if result == 0 else "Benign"

    return {
        "prediction": int(result),
        "label": label
    }