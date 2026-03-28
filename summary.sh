#!/bin/bash
mkdir -p results

docker cp pipeline-container:/app/pipeline/data_raw.csv results/
docker cp pipeline-container:/app/pipeline/data_preprocessed.csv results/
docker cp pipeline-container:/app/pipeline/insight1.txt results/
docker cp pipeline-container:/app/pipeline/insight2.txt results/
docker cp pipeline-container:/app/pipeline/insight3.txt results/
docker cp pipeline-container:/app/pipeline/summary_plot.png results/
docker cp pipeline-container:/app/pipeline/clusters.txt results/
docker cp pipeline-container:/app/pipeline/pairplot.png results/
docker cp pipeline-container:/app/pipeline/heatmap.png results/
docker cp pipeline-container:/app/pipeline/histogram.png results/

echo "saved outputs to results/"

docker stop pipeline-container
docker rm pipeline-container

echo "removed container"
 