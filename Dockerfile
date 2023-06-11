# Pull base image
FROM python:3.9-slim

# Upgrade pip
RUN pip install --upgrade pip

# Set work directory
WORKDIR /binance_flask

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .