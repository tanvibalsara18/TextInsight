# Use the official Python 3.8 slim image to reduce image size
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements.txt file first to utilize caching of dependencies
COPY requirements.txt /app/

# Install dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Optional: Clean up and uninstall unnecessary packages if needed
# RUN pip uninstall -y transformers accelerate && \
#     pip install transformers accelerate

# Set the command to run your application (ensure app.py is present)
CMD ["python3", "app.py"]
