# Use an official lightweight Python image
FROM python:3.11-slim

# Prevent Python from writing pyc files to disc and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies if needed (uncomment if your app requires build tools)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy and install Python dependencies first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .


# ENTRYPOINT defines the base command that always runs
ENTRYPOINT ["python", "caching-proxy.py"]