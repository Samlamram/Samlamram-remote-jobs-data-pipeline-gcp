# Remote Jobs Data Pipeline on GCP

Pipeline end-to-end de Data Engineering construido en Google Cloud Platform para extraer vacantes remotas desde una API pública, almacenar datos raw en Cloud Storage, transformar la información y cargarla en BigQuery para análisis.

## Objetivo

Demostrar fundamentos reales de data engineering en un proyecto sencillo pero completo:

- extracción desde API
- almacenamiento raw en cloud
- transformación de datos
- carga a BigQuery
- modelado por capas
- pruebas, linting y CI
- flujo de trabajo con ramas y pull requests

## Fuente de datos

- API pública de Remotive

## Arquitectura

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