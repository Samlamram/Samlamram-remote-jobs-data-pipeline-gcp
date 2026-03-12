def transform_jobs(raw_jobs):
    transformed_jobs = []

    for job in raw_jobs:
        company_name = job.get("company_name")
        location = job.get("candidate_required_location")
        salary = job.get("salary")

        if company_name:
            company_name_clean = company_name.strip()
        else:
            company_name_clean = None

        if location:
            location_lower = location.lower()

            if "worldwide" in location_lower:
                location_type = "worldwide"
            elif "remote" in location_lower:
                location_type = "remote"
            else:
                location_type = "restricted"
        else:
            location_type = "unknown"

        has_salary = bool(salary and str(salary).strip())

        transformed_job = {
            "id": job.get("id"),
            "title": job.get("title"),
            "company_name": company_name,
            "company_name_clean": company_name_clean,
            "category": job.get("category"),
            "job_type": job.get("job_type"),
            "publication_date": job.get("publication_date"),
            "candidate_required_location": location,
            "location_type": location_type,
            "salary": salary,
            "has_salary": has_salary,
            "url": job.get("url")
        }

        transformed_jobs.append(transformed_job)

    return transformed_jobs
