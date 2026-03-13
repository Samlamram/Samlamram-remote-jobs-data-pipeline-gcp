from google.cloud import bigquery
from config import GCP_PROJECT_ID, BQ_DATASET_ID, BQ_TABLE_ID


def get_table_id():
    return f"{GCP_PROJECT_ID}.{BQ_DATASET_ID}.{BQ_TABLE_ID}"


def get_temp_table_id():
    return f"{GCP_PROJECT_ID}.{BQ_DATASET_ID}.{BQ_TABLE_ID}_temp"


def get_schema():
    return [
        bigquery.SchemaField("id", "INT64"),
        bigquery.SchemaField("title", "STRING"),
        bigquery.SchemaField("company_name", "STRING"),
        bigquery.SchemaField("company_name_clean", "STRING"),
        bigquery.SchemaField("category", "STRING"),
        bigquery.SchemaField("job_type", "STRING"),
        bigquery.SchemaField("publication_date", "STRING"),
        bigquery.SchemaField("candidate_required_location", "STRING"),
        bigquery.SchemaField("location_type", "STRING"),
        bigquery.SchemaField("salary", "STRING"),
        bigquery.SchemaField("has_salary", "BOOL"),
        bigquery.SchemaField("url", "STRING"),
    ]


def ensure_table_exists():
    client = bigquery.Client(project=GCP_PROJECT_ID)
    table_id = get_table_id()
    table = bigquery.Table(table_id, schema=get_schema())

    try:
        client.get_table(table_id)
        print(f"Tabla ya existe en BigQuery: {table_id}")
    except Exception:
        client.create_table(table)
        print(f"Tabla creada en BigQuery: {table_id}")


def recreate_temp_table():
    client = bigquery.Client(project=GCP_PROJECT_ID)
    temp_table_id = get_temp_table_id()

    try:
        client.delete_table(temp_table_id, not_found_ok=True)
    except Exception:
        pass

    temp_table = bigquery.Table(temp_table_id, schema=get_schema())
    client.create_table(temp_table)
    print(f"Tabla temporal creada en BigQuery: {temp_table_id}")


def load_jobs_to_temp_table(rows):
    client = bigquery.Client(project=GCP_PROJECT_ID)
    temp_table_id = get_temp_table_id()

    job_config = bigquery.LoadJobConfig(
        schema=get_schema(),
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    load_job = client.load_table_from_json(
        rows,
        temp_table_id,
        job_config=job_config,
        location="us-central1",
    )

    load_job.result()
    print(f"Filas cargadas en tabla temporal: {len(rows)} en {temp_table_id}")


def merge_temp_into_target():
    client = bigquery.Client(project=GCP_PROJECT_ID)
    target_table = get_table_id()
    temp_table = get_temp_table_id()

    merge_sql = f"""
    MERGE `{target_table}` AS target
    USING `{temp_table}` AS source
    ON target.id = source.id
    WHEN MATCHED THEN
      UPDATE SET
        title = source.title,
        company_name = source.company_name,
        company_name_clean = source.company_name_clean,
        category = source.category,
        job_type = source.job_type,
        publication_date = source.publication_date,
        candidate_required_location = source.candidate_required_location,
        location_type = source.location_type,
        salary = source.salary,
        has_salary = source.has_salary,
        url = source.url
    WHEN NOT MATCHED THEN
      INSERT (
        id,
        title,
        company_name,
        company_name_clean,
        category,
        job_type,
        publication_date,
        candidate_required_location,
        location_type,
        salary,
        has_salary,
        url
      )
      VALUES (
        source.id,
        source.title,
        source.company_name,
        source.company_name_clean,
        source.category,
        source.job_type,
        source.publication_date,
        source.candidate_required_location,
        source.location_type,
        source.salary,
        source.has_salary,
        source.url
      )
    """

    query_job = client.query(merge_sql)
    query_job.result()
    print(f"MERGE completado hacia {target_table}")


def drop_temp_table():
    client = bigquery.Client(project=GCP_PROJECT_ID)
    temp_table_id = get_temp_table_id()
    client.delete_table(temp_table_id, not_found_ok=True)
    print(f"Tabla temporal eliminada: {temp_table_id}")