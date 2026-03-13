from google.cloud import bigquery
from config import GCP_PROJECT_ID


def run_sql_file(file_path):
    client = bigquery.Client(project=GCP_PROJECT_ID)

    with open(file_path, "r", encoding="utf-8") as file:
        query = file.read()

    query_job = client.query(query, location="us-central1")
    query_job.result()

    print(f"SQL ejecutado correctamente desde: {file_path}")
