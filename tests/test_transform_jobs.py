from app.transform.transform_jobs import transform_jobs


def test_transform_jobs_returns_expected_fields():
    raw_jobs = [
        {
            "id": 1,
            "title": "Data Engineer",
            "company_name": " ACME ",
            "category": "Software Development",
            "job_type": "full_time",
            "publication_date": "2026-03-12T10:00:00",
            "candidate_required_location": "Worldwide",
            "salary": "$100k",
            "url": "https://example.com/job/1"
        }
    ]

    result = transform_jobs(raw_jobs)

    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["title"] == "Data Engineer"
    assert result[0]["company_name"] == " ACME "
    assert result[0]["company_name_clean"] == "ACME"
    assert result[0]["location_type"] == "worldwide"
    assert result[0]["has_salary"] is True