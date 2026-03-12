from config import PROJECT_NAME
from extract.jobs_api import fetch_jobs
from file_loader import (
    save_raw_data_to_json,
    save_transformed_jobs_to_json,
    save_summary_to_json
)
from transform.transform_jobs import transform_jobs
from utils.summary import build_summary_data


def main():
    print(f"Proyecto: {PROJECT_NAME}")

    raw_data, jobs_preview = fetch_jobs()

    raw_jobs = raw_data["jobs"]
    transformed_jobs = transform_jobs(raw_jobs)
    summary_data = build_summary_data(raw_jobs, transformed_jobs)

    print(f"\nTotal de vacantes raw encontradas: {summary_data['total_raw_jobs']}")
    print(f"Total de vacantes transformadas: {summary_data['total_transformed_jobs']}\n")

    print("Resumen del pipeline:")
    print(f"- Vacantes con salario: {summary_data['jobs_with_salary']}")
    print(f"- Vacantes worldwide: {summary_data['worldwide_jobs']}")
    print(f"- Vacantes remote: {summary_data['remote_jobs']}")
    print(f"- Vacantes restricted: {summary_data['restricted_jobs']}\n")

    print("Vacantes por categoría:")
    for category, count in summary_data["categories"].items():
        print(f"- {category}: {count}")
    print()

    print("Primeras 3 vacantes transformadas:\n")

    for job in transformed_jobs[:3]:
        print(f"ID: {job['id']}")
        print(f"Título: {job['title']}")
        print(f"Empresa: {job['company_name']}")
        print(f"Empresa limpia: {job['company_name_clean']}")
        print(f"Categoría: {job['category']}")
        print(f"Tipo: {job['job_type']}")
        print(f"Fecha publicación: {job['publication_date']}")
        print(f"Ubicación: {job['candidate_required_location']}")
        print(f"Tipo de ubicación: {job['location_type']}")
        print(f"Salario: {job['salary']}")
        print(f"Tiene salario: {job['has_salary']}")
        print(f"URL: {job['url']}")
        print("-" * 50)

    save_raw_data_to_json(raw_data)
    save_transformed_jobs_to_json(transformed_jobs)
    save_summary_to_json(summary_data)


if __name__ == "__main__":
    main()
