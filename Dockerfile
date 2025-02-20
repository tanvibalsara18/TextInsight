FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y \
    gcc g++ make wget curl git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install --default-timeout=100 -r requirements.txt && \
    pip install --upgrade accelerate 

COPY . /app

CMD ["python3", "app.py"]
