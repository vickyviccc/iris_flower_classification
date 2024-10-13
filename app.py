import joblib
from fastapi import FastAPI

app = FastAPI()

# Load the model at the start of the app
model = joblib.load("iris_knn_model.pkl")

@app.get("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    # Create a feature array for the prediction
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    
    # Get the prediction from the model
    prediction = model.predict(features)[0]
    
    return {"prediction": prediction}
