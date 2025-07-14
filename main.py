import mlflow
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime

app = FastAPI(
    title="Water Potability Prediction API",
    description="API for predicting water potability using a trained model.",
)

# Serve UI
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

# Enable CORS so frontend JS can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# MLflow tracking URI
dagshub_url = "https://dagshub.com"
repo_owner = "irfanshaikh911"
repo_name = "CI_MLOPS"
mlflow.set_tracking_uri(f"{dagshub_url}/{repo_owner}/{repo_name}.mlflow")

def load_model():
    client = mlflow.tracking.MlflowClient()
    versions = client.get_latest_versions("Best Model", stages=["Production"])
    run_id = versions[0].run_id
    print(f"Loaded model from run: {run_id}")
    return mlflow.pyfunc.load_model(f"runs:/{run_id}/Best Model")

model = load_model()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/predict")
async def predict(request: Request):
    input_data = await request.json()
    
    # Ensure float conversion for all inputs
    input_data = {key: float(value) for key, value in input_data.items()}
    
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    # Optional: Add probability if model supports it
    probability = 0.85  # Replace if your model provides it

    response = {
        "prediction": "Potable" if prediction == 1 else "Not Potable",
        "probability": probability,
        "model_used": "MLflow Model",
        "timestamp": datetime.now().isoformat(),
        "feature_importance": [
            {"feature": col, "importance": round(1 / df.shape[1], 2)}
            for col in df.columns
        ]
    }

    return JSONResponse(content=response)


@app.get("/api/metrics")
def metrics():
    with open("reports/metrics.json", "r") as f:
        metrics = json.load(f)

    return {
        "model": "MLflow Model",
        "metrics": metrics
    }
