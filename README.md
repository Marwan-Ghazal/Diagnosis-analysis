# Diagnosis Analysis Project

This project takes patient data and does all the stuff—ingesting, cleaning, analyzing, clustering, and making plots using Python and Docker.

## What You Need

- Docker installed on your system
- Patient dataset CSV file (e.g., `patient_dataset.csv`)

## Docker Setup

### Build the Docker Image

```bash
docker build -t diagnosis-analysis .
```

### Run the Container

```bash
docker run -it --name diagnosis-container diagnosis-analysis
```

Once inside, you can run the scripts one by one:

1. **Data Ingestion**
   ```bash
   python ingest.py patient_dataset.csv
   ```
   - Input: Raw patient dataset CSV
   - Output: `data_raw.csv` (raw data saved)

2. **Data Preprocessing**
   ```bash
   python preprocess.py data_raw.csv
   ```
   - Input: `data_raw.csv`
   - Output: `data_preprocessed.csv` (cleaned and preprocessed data)

3. **Analytics and Insights**
   ```bash
   python analytics.py data_preprocessed.csv
   ```
   - Input: `data_preprocessed.csv`
   - Outputs: `insight1.txt`, `insight2.txt`, `insight3.txt` (text files with analysis insights)

4. **Clustering**
   ```bash
   python cluster.py data_preprocessed.csv
   ```
   - Input: `data_preprocessed.csv`
   - Output: `clusters.txt` (clustering results)

5. **Visualization**
   ```bash
   python visualize.py data_preprocessed.csv
   python visualizee.py data_preprocessed.csv
   ```
   - Input: `data_preprocessed.csv`
   - Outputs: Various `.png` files (plots and charts)

### After running all scripts, use the provided `summary.sh` script to copy all outputs to the host machine:

```bash
./summary.sh
```

This will:
- Copy all `.csv`, `.txt`, and `.png` files to `customer-analytics/results/` on the host
- Stop and remove the container

## Notes

- Ensure the container is running before executing the scripts.
- All outputs are generated in the `/app/pipeline/` directory inside the container.

## Team Members:

- Jannah Ashraf (231001399)
- Marwan Ghazal (231000765)
- Omar Abdelrazek (231000573)
- Abdulmonem Demerdash (231000114)

---
[Dockerhub image link](https://hub.docker.com/repository/docker/jannahhhh/diagnosis-analytics/general)

[Github link](https://github.com/Marwan-Ghazal/Diagnosis-analysis)