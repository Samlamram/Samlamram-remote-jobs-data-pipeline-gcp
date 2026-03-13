CREATE OR REPLACE TABLE `remote-jobs-pipeline.jobs_mart.remote_jobs_mart` AS
SELECT
    id,
    title,
    company_name_clean AS company_name,
    category,
    job_type,
    location_type,
    has_salary,
    publication_date,
    DATE(SUBSTR(publication_date, 1, 10)) AS publication_date_only,
    url
FROM `remote-jobs-pipeline.jobs_staging.remote_jobs`;