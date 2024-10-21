# DVC Demo Project

This repository demonstrates the usage of DVC (Data Version Control) for managing machine learning workflows. It provides a structured approach to data processing, feature engineering, model training, and evaluation while utilizing Google Cloud Storage for remote storage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version >= 3.6)
- [DVC](https://dvc.org/doc/install) (install via pip)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/dvc-demo.git
cd dvc-demo
pip install -r requirements.txt
```

## Usage

This project consists of several stages, each representing a step in the data processing and model training pipeline. Here’s how to set up each stage using DVC:

1. **Preprocess Data**:
   ```bash
   dvc stage add -n preprocess \
       -d src/data/preprocess.py -d data/raw/data.csv \
       -o data/processed/preprocessed_data.csv \
       python src/data/preprocess.py data/raw/data.csv data/processed/preprocessed_data.csv
   ```

2. **Build Features**:
   ```bash
   dvc stage add -n build_features \
       -d src/features/build_features.py -d data/processed/preprocessed_data.csv \
       -o data/processed/features.csv \
       python src/features/build_features.py data/processed/preprocessed_data.csv data/processed/features.csv
   ```

3. **Train Model**:
   ```bash
   dvc stage add -n train_model \
       -d src/models/train.py -d data/processed/features.csv -d params.yaml \
       -o models/model.pkl -o metrics.txt \
       python src/models/train.py data/processed/features.csv models/model.pkl --params params.yaml
   ```

4. **Evaluate Model**:
   ```bash
   dvc stage add -n evaluate_model \
       -d src/models/evaluate.py -d models/model.pkl -d data/raw/data.csv \
       -M metrics.txt \
       python src/models/evaluate.py models/model.pkl data/raw/data.csv metrics.txt
   ```

## Configuration

To configure your DVC remote storage with Google Cloud, authenticate and set up the remote:

1. **Authenticate with Google Cloud**:
   ```bash
   gcloud auth login
   gcloud auth application-default login
   ```

2. **Add a DVC Remote**:
   ```bash
   dvc remote add -d myremote gs://my-dvc-bucket/path
   dvc remote modify myremote credentialpath ~/.config/gcloud/application_default_credentials.json
   ```

This sets up the DVC remote to use your Google Cloud Storage bucket for storing datasets and model files.



