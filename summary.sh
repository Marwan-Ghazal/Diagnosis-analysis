#!/bin/bash

IMAGE_NAME="diagnosis-analysis"
CONTAINER_NAME="diagnosis-pipeline"

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

echo "Running pipeline in container..."
docker run --name $CONTAINER_NAME $IMAGE_NAME

echo "Copying results to host..."
mkdir -p results
docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv results/
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv results/
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt results/
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt results/
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt results/
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png results/
docker cp $CONTAINER_NAME:/app/pipeline/results/clusters.txt results/

echo "Results saved to ./results/"
ls -la results/

docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

echo "Done!"
