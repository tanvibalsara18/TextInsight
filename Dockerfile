FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --upgrade accelerate
RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]
