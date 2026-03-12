from config import PROJECT_NAME
from extract.jobs_api import fetch_jobs
from file_loader import (
    save_raw_data_to_json,
    save_transformed_jobs_to_json,
    save_summary_to_json
)
from transform.transform_jobs import transform_jobs

def count_jobs_by_category(jobs):
    category_count = {}

    for job in jobs:
        category = job["category"]

        if not category:
            category = "Unknown"

        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1

    return category_count

def main():
    print(f"Proyecto: {PROJECT_NAME}")

    raw_data, jobs_preview = fetch_jobs()

    raw_jobs = raw_data["jobs"]
    transformed_jobs = transform_jobs(raw_jobs)
    category_count = count_jobs_by_category(transformed_jobs)

    total_jobs = len(transformed_jobs)
    jobs_with_salary = sum(1 for job in transformed_jobs if job["has_salary"])
    worldwide_jobs = sum(1 for job in transformed_jobs if job["location_type"] == "worldwide")
    remote_jobs = sum(1 for job in transformed_jobs if job["location_type"] == "remote")
    restricted_jobs = sum(1 for job in transformed_jobs if job["location_type"] == "restricted")

    summary_data = {
        "total_raw_jobs": len(raw_jobs),
        "total_transformed_jobs": len(transformed_jobs),
        "jobs_with_salary": jobs_with_salary,
        "worldwide_jobs": worldwide_jobs,
        "remote_jobs": remote_jobs,
        "restricted_jobs": restricted_jobs,
        "categories": category_count
    }

    print(f"\nTotal de vacantes raw encontradas: {len(raw_jobs)}")
    print(f"Total de vacantes transformadas: {len(transformed_jobs)}\n")

    print("Resumen del pipeline:")
    print(f"- Vacantes con salario: {jobs_with_salary}")
    print(f"- Vacantes worldwide: {worldwide_jobs}")
    print(f"- Vacantes remote: {remote_jobs}")
    print(f"- Vacantes restricted: {restricted_jobs}\n")

    print("Vacantes por categoría:")
    for category, count in category_count.items():
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