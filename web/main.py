# from fastapi import FastAPI, Request
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib
import json
import pandas as pd
from datetime import datetime

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="web/static"), name="static")

# Serve templates (HTML)
templates = Jinja2Templates(directory="web/templates")

# Load model
model = joblib.load("models/model.pkl")

# Define expected input using Pydantic
class WaterInput(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Sulfate: float
    Conductivity: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float

# Serve the UI
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API for prediction
@app.post("/api/predict")
async def predict(request: Request):
    input_data = await request.json()
    input_data = {key: float(value) for key, value in input_data.items()}
    df = pd.DataFrame([input_data])
    
    prediction = model.predict(df)[0]
    probability = 0.85  # Optional static confidence

    return JSONResponse({
        "prediction": "Potable" if prediction == 1 else "Not Potable",
        "probability": probability,
        "model_used": "RandomForest",
        "timestamp": datetime.now().isoformat(),
        "feature_importance": [
            {"feature": col, "importance": round(1 / len(df.columns), 2)}
            for col in df.columns
        ]
    })
    
@app.get("/api/metrics")
async def get_metrics():
    try:
        with open("metrics.json", "r") as f:
            metrics = json.load(f)
        return {
            "metrics": metrics,
            "model": "RandomForest"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not load metrics: {e}")

# Optional: Add /api/metrics if using evaluation
