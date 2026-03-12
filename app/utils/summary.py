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


def build_summary_data(raw_jobs, transformed_jobs):
    category_count = count_jobs_by_category(transformed_jobs)

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

    return summary_data