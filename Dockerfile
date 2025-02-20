FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app/

# Install system dependencies (only necessary ones)
RUN apt-get update && apt-get install -y \
    gcc g++ make wget curl git && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies, forcing CPU version of torch
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --default-timeout=1200 -r requirements.txt

COPY . /app

CMD ["python3", "app.py"]
