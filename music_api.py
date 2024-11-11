from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Initialize the FastAPI app
app = FastAPI(title="Music Popularity Prediction API", description="API for predicting song popularity class using a trained ensemble model")

# === Model ===
# Load the trained stacking model
model = joblib.load('stacking_model.joblib')


# Define feature columns to maintain consistent input order
FEATURE_COLUMNS = [
    'Popularity', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 
    'duration_in min/ms', 'time_signature'
]

# === View ===
# Define input data structure using Pydantic
class SongFeatures(BaseModel):
    Popularity: float
    danceability: float
    energy: float
    key: float
    loudness: float
    mode: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration_in_min_ms: float
    time_signature: int

# === Controller ===
@app.post("/predict", response_model=dict)
async def predict(song: SongFeatures):
    """
    Predict the popularity class of a song based on its features.
    """
    # Convert the incoming data to a DataFrame with appropriate feature order
    input_data = pd.DataFrame([[song.Popularity, song.danceability, song.energy, song.key,
                                song.loudness, song.mode, song.speechiness, song.acousticness,
                                song.instrumentalness, song.liveness, song.valence, song.tempo,
                                song.duration_in_min_ms, song.time_signature]],
                              columns=FEATURE_COLUMNS)
    
    # Predict the class using the model
    try:
        prediction = model.predict(input_data)
        return {"predicted_class": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Music Popularity Prediction API"}

# Start the app with: uvicorn filename:app --reload
