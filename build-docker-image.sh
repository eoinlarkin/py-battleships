#!/bin/bash

# Variables
IMAGE_NAME="py-battleships"
CONTAINER_NAME="py-battleships"
PORT=8000
TAG="latest"
NO_CACHE=false # Default: caching enabled

# Function to display usage
usage() {
    echo "Usage: $0 [--run]"
    echo "  --run    Start the container after building the image"
    echo "  --tag <tag>    Specify a custom tag for the Docker image (default: latest)"
    echo "  --no-cache     Disable Docker build cache"
    exit 1
}

# Parse arguments
RUN_CONTAINER=false
while [[ $# -gt 0 ]]; do
    case $1 in
        --run)
            RUN_CONTAINER=true
            shift
            ;;
        --tag)
            if [[ -n $2 ]]; then
                TAG=$2
                shift 2
            else
                echo "Error: --tag requires a value"
                usage
            fi
            ;;
        --no-cache)
            NO_CACHE=true
            shift
            ;;
        *)
            usage
            ;;
    esac
done

# Build the Docker image
echo "Building the Docker image..."
if [ "$NO_CACHE" = true ]; then
    docker build --no-cache -t $IMAGE_NAME:$TAG .
else
    docker build -t $IMAGE_NAME:$TAG .
fi

if [ $? -ne 0 ]; then
    echo "Error: Failed to build the Docker image."
    exit 1
fi
echo "Docker image built successfully: $IMAGE_NAME:$TAG"

# Optionally run the container
if [ "$RUN_CONTAINER" = true ]; then
    # Check if a container with the same name already exists
    if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
        echo "Stopping and removing existing container: $CONTAINER_NAME"
        docker stop $CONTAINER_NAME
        docker rm $CONTAINER_NAME
    fi

    echo "Starting the container..."
    docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME:$TAG

    if [ $? -ne 0 ]; then
        echo "Error: Failed to start the container."
        exit 1
    fi
    echo "Container started successfully: $CONTAINER_NAME"
    echo "Access the application at http://localhost:$PORT"
fi