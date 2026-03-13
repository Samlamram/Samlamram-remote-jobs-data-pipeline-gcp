import requests


def fetch_jobs():
    print("Trayendo vacantes desde la API...")

    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    raw_data = response.json()
    jobs = raw_data["jobs"]

    jobs_simplified = []

    for job in jobs:
        jobs_simplified.append(
            {
                "id": job["id"],
                "title": job["title"],
                "company": job["company_name"],
                "location": job["candidate_required_location"]
            }
        )

    return raw_data, jobs_simplified
