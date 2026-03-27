#!/bin/bash

# Create the results directory on the host if it doesn't exist
mkdir -p customer-analytics/results/

# Copy all generated outputs (.csv, .txt, .png) from the container to the host
docker cp diagnosis-container:/app/pipeline/*.csv customer-analytics/results/
docker cp diagnosis-container:/app/pipeline/*.txt customer-analytics/results/
docker cp diagnosis-container:/app/pipeline/*.png customer-analytics/results/

# Stop and remove the running container
docker stop diagnosis-container
docker rm diagnosis-container

echo "Outputs copied to customer-analytics/results/ and container stopped and removed."
