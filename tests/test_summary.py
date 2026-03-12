from app.utils.summary import build_summary_data


def test_build_summary_data_counts_correctly():
    raw_jobs = [
        {"id": 1},
        {"id": 2},
        {"id": 3}
    ]

    transformed_jobs = [
        {
            "category": "Software Development",
            "has_salary": True,
            "location_type": "worldwide"
        },
        {
            "category": "Software Development",
            "has_salary": False,
            "location_type": "restricted"
        },
        {
            "category": "Marketing",
            "has_salary": True,
            "location_type": "remote"
        }
    ]

    summary = build_summary_data(raw_jobs, transformed_jobs)

    assert summary["total_raw_jobs"] == 3
    assert summary["total_transformed_jobs"] == 3
    assert summary["jobs_with_salary"] == 2
    assert summary["worldwide_jobs"] == 1
    assert summary["remote_jobs"] == 1
    assert summary["restricted_jobs"] == 1
    assert summary["categories"]["Software Development"] == 2
    assert summary["categories"]["Marketing"] == 1