# Use a lightweight Python base image
FROM python:3.8-slim-buster

# Set working directory inside the container
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt .

# Upgrade pip and install dependencies efficiently
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=300 -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu/ && \
    pip install --no-cache-dir --upgrade accelerate

# Copy the rest of the application files
COPY . .

# Default command to run the application
CMD ["python3", "app.py"]