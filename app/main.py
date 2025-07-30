from fastapi import FastAPI
from pydantic import BaseModel, conlist
from typing import List
from prediction import make_prediction
import config

app = FastAPI(
    title="API Peramalan Beban Listrik",
    description="API untuk memprediksi beban listrik jangka pendek di Jawa Timur menggunakan model Hybrid LSTM-ANN.",
    version="1.0.0"
)

# Pydantic model untuk validasi input
# Memastikan input adalah list float dengan panjang tepat IN_STEPS
class PowerLoadInput(BaseModel):
    historical_load: conlist(float, min_length=config.IN_STEPS, max_length=config.IN_STEPS)

@app.get("/", tags=["General"])
def read_root():
    return {"message": "Selamat datang di API Peramalan Beban Listrik"}

@app.post("/predict", tags=["Prediction"])
def predict_load(data: PowerLoadInput) -> dict:
    """
    Endpoint untuk melakukan peramalan beban listrik.

    - **Input**: `historical_load` (list float) - Data historis beban listrik selama 24 jam terakhir (48 data point).
    - **Output**: JSON berisi `forecast` (list float) - Prediksi beban listrik untuk 24 jam ke depan.
    """
    prediction = make_prediction(raw_input=data.historical_load)
    return prediction