FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for LightGBM
RUN apt-get update && apt-get install -y \
    gcc \
    libgomp1

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the application files
COPY music_api.py .
COPY stacking_model.joblib .

# Debug: List all files in /app to confirm they're copied
RUN ls -al /app

# Run the application with uvicorn
CMD ["uvicorn", "music_api:app", "--host", "0.0.0.0", "--port", "8000"]
