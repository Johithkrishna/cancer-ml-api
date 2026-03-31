from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

# Define input schema
class Features(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: Features):
    try:
        features_array = np.array(data.features).reshape(1, -1)
        prediction = model.predict(features_array)
        return {"prediction": int(prediction[0])}
    
    except Exception as e:
        return {"error": str(e)}