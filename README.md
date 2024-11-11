# Music Popularity Prediction API

This project is a web API to predict the popularity class of a song based on its features, using a pre-trained ensemble model.

## Features
- Predicts song popularity based on attributes like danceability, energy, tempo, and more.
- Built with FastAPI and Docker for easy deployment.

## Docker Hub Image
You can find the pre-built Docker image on Docker Hub here: [Music API Docker Hub](https://hub.docker.com/r/andrewvictor01/music-api).

### Pull the Docker Image
To pull the Docker image from Docker Hub, run:
```sh
docker pull andrewvictor01/music-api
```

## Requirements
- Python 3.9+
- Docker (if you want to run using Docker)

All required Python libraries are listed in `requirements.txt`.

## Setup and Usage

### Running with Docker
1. Clone this repository:
   ```sh
   git clone https://github.com/andrewvictor01/music-api-project.git
   cd music-api-project
   ```
2. Pull the Docker image from Docker Hub:
   ```sh
   docker pull andrewvictor01/music-api
   ```
3. Run the Docker container:
   ```sh
   docker run -d -p 8000:8000 --name music_api_container andrewvictor01/music-api
   ```
4. Visit `http://localhost:8000/docs` to interact with the API documentation.

### Running without Docker
1. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
2. Run the API:
   ```sh
   uvicorn music_api:app --reload
   ```

## API Endpoints
### `POST /predict`
- **Description**: Predict the popularity class of a song based on its features.
- **Input**: JSON object with the following attributes:
  - `Popularity` (number): Current popularity rating (0-100).
  - `danceability` (number): How suitable the track is for dancing (0-1).
  - `energy` (number): Energy of the song (0-1).
  - `key` (number): The key of the song (0-11).
  - `loudness` (number): The overall loudness of the track in dB.
  - `mode` (integer): The modality (0 = minor, 1 = major).
  - `speechiness` (number): Speechiness metric (0-1).
  - `acousticness` (number): Acousticness metric (0-1).
  - `instrumentalness` (number): Whether the track is instrumental (0-1).
  - `liveness` (number): The probability of a live audience (0-1).
  - `valence` (number): The musical positivity (0-1).
  - `tempo` (number): The overall tempo of the song in BPM.
  - `duration_in_min_ms` (number): Duration of the track in milliseconds.
  - `time_signature` (integer): The time signature of the track.
- **Output**: Predicted popularity class.

## Example Request
```json
{
  "Popularity": 50,
  "danceability": 0.8,
  "energy": 0.7,
  "key": 5,
  "loudness": -6.5,
  "mode": 1,
  "speechiness": 0.04,
  "acousticness": 0.2,
  "instrumentalness": 0,
  "liveness": 0.15,
  "valence": 0.75,
  "tempo": 120,
  "duration_in_min_ms": 210000,
  "time_signature": 4
}
```

## License
This project is licensed under the MIT License.

