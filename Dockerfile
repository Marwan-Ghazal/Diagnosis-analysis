FROM python:3.11-slim

RUN pip install --no-cache-dir \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    scipy

COPY . /app/pipeline/

WORKDIR /app/pipeline/

CMD python ingest.py patient_dataset.csv && \
    python preprocess.py data_raw.csv && \
    python analytics.py data_preprocessed.csv && \
    python visualize.py data_preprocessed.csv