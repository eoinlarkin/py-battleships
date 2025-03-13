#!/bin/bash

# Variables
PROJECT_ID="py-battleships"
IMAGE_NAME="py-battleships"
SERVICE_NAME="py-battleships-service"
REGION="europe-west1"

# Authenticate with Google Cloud
gcloud auth login

# Set the active project
gcloud config set project $PROJECT_ID

# Authenticate Docker to Google Container Registry
gcloud auth configure-docker

# Build the Docker image
docker build -t gcr.io/$PROJECT_ID/$IMAGE_NAME:latest .

# Push the Docker image to Google Container Registry
docker push gcr.io/$PROJECT_ID/$IMAGE_NAME:latest

# Deploy the Docker image to Google Cloud Run
gcloud run deploy $SERVICE_NAME --image gcr.io/$PROJECT_ID/$IMAGE_NAME:latest --platform managed --region $REGION

echo "Deployment complete. Your service is now running on Google Cloud Run."