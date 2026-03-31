import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "model.pkl")

model = joblib.load(model_path)

def predict(features):
    arr = np.array(features).reshape(1, -1)
    return model.predict(arr)[0]