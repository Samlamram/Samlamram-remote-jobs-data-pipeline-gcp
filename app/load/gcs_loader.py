from google.cloud import storage
from config import GCS_BUCKET_NAME


def upload_file_to_gcs(local_file_path, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET_NAME)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(local_file_path)

    print(f"Archivo subido a GCS: gs://{GCS_BUCKET_NAME}/{destination_blob_name}")
