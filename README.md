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

## Architecture diagram

```mermaid
flowchart TD
    A[Remotive API] --> B[Python Pipeline]
    B --> C[Raw JSON local]
    C --> D[Google Cloud Storage<br/>raw layer]
    B --> E[Transformed Jobs]
    E --> F[BigQuery Staging<br/>jobs_staging.remote_jobs]
    F --> G[BigQuery Mart<br/>jobs_mart.remote_jobs_mart]
    H[Docker Image] --> I[Artifact Registry]
    I --> J[Cloud Run Job]
    K[Cloud Scheduler] --> J
    J --> D
    J --> F
    J --> G


## Qué representa

- la API como fuente
- el pipeline en Python como motor
- raw en GCS
- staging y mart en BigQuery
- Docker + Artifact Registry
- Cloud Run Job como ejecución cloud
- Cloud Scheduler como disparador automático

## Siguiente mejora útil

Después de eso, yo haría una sección cortica tipo **“How the cloud execution works”**.

Puedes agregar esto también al README:

```md
## Cloud execution flow

1. Cloud Scheduler triggers the Cloud Run Job
2. Cloud Run executes the containerized Python pipeline
3. The pipeline extracts jobs from the Remotive API
4. Raw data is stored in Cloud Storage
5. Transformed data is merged into BigQuery staging
6. SQL is executed to refresh the mart table