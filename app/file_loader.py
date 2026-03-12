import json
from datetime import datetime

def save_raw_data_to_json(raw_data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"data/raw_jobs_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(raw_data, file, indent=4, ensure_ascii=False)

    print(f"Raw data guardada en {file_path}")


def save_transformed_jobs_to_json(transformed_jobs):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"data/transformed_jobs_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(transformed_jobs, file, indent=4, ensure_ascii=False)

    print(f"Data transformada guardada en {file_path}")

def save_summary_to_json(summary_data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"data/summary_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(summary_data, file, indent=4, ensure_ascii=False)

    print(f"Resumen guardado en {file_path}")