from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

# Load model
model = joblib.load("iris_knn_model.pkl")

# Input model
class IrisData(BaseModel):
    data: list

@app.post("/predict")
async def predict(iris_data: IrisData):
    new_data = np.array(iris_data.data)
    prediction = model.predict(new_data).tolist()
    return {"prediction": prediction}
