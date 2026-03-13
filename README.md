# Remote Jobs Data Pipeline on GCP

End-to-end Data Engineering project built on Google Cloud Platform to extract remote job postings from a public API, store raw data in Cloud Storage, transform it, load it into BigQuery, and materialize an analytical mart for reporting and analysis.

## Project goal

This project was built to demonstrate practical Data Engineering fundamentals in a simple but realistic architecture:

- data extraction from a public API
- raw storage in cloud
- transformation and standardization
- loading into BigQuery
- layered modeling (raw / staging / mart)
- containerization with Docker
- orchestration with Cloud Run Jobs
- scheduled execution with Cloud Scheduler
- tests, linting, CI, and branching strategy

## Data source

- Remotive public jobs API

## Architecture

```text
Remotive API
   ↓
Python pipeline
   ↓
Raw JSON local
   ↓
Google Cloud Storage (raw layer)
   ↓
BigQuery staging (jobs_staging.remote_jobs)
   ↓
BigQuery mart (jobs_mart.remote_jobs_mart)
   ↓
Cloud Run Job
   ↓
Cloud Scheduler
