import os

PROJECT_NAME = "Remote Jobs Data Pipeline"
GCP_PROJECT_ID = "remote-jobs-pipeline"
GCS_BUCKET_NAME = "remote-jobs-pipeline-raw-samlamram"
BQ_DATASET_ID = "jobs_staging"
BQ_TABLE_ID = "remote_jobs"

ENABLE_GCS_UPLOAD = os.getenv("ENABLE_GCS_UPLOAD", "false").lower() == "true"
ENABLE_BQ_LOAD = os.getenv("ENABLE_BQ_LOAD", "false").lower() == "true"