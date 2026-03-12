# Remote Jobs Data Pipeline on GCP

Proyecto sencillo de Data Engineering para extraer vacantes remotas desde una API pública, guardar datos raw, transformar la información y dejarla lista para análisis.

## Objetivo

Construir un pipeline básico pero bien organizado que demuestre fundamentos reales de data engineering:

- extracción desde API
- almacenamiento raw
- transformación de datos
- estructura por capas
- base para migrar luego a GCP

## Fuente de datos

- API pública de Remotive

## Qué hace actualmente

El proyecto actualmente:

1. consulta la API de vacantes
2. guarda la respuesta raw en JSON
3. transforma campos importantes
4. guarda la data transformada en JSON
5. genera un resumen de la ejecución

## Estructura del proyecto

```text
remote-jobs-data-pipeline-gcp/
├── app/
│   ├── extract/
│   │   └── jobs_api.py
│   ├── transform/
│   │   └── transform_jobs.py
│   ├── config.py
│   ├── file_loader.py
│   └── main.py
├── data/
├── requirements.txt
├── .gitignore
└── README.md