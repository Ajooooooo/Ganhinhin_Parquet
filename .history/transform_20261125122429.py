import duckdb

duckdb.sql("""
COPY(
    SELECT DISTINCT
        session_id,
        session_date,
        customer_id,
        store_id,
        device_type,
        SPLIT_PART(browser_os), '|', 1) AS browser,
        SPLIT_PART(browser_os), '|', 2) AS os,
        session_purchase_made,
        session_duration_minutes,
        session_pages_visited,
        COALESCE(session_quality_score, avg(session_quality_score) over()) AS session_quality_score,
    From 'extract.parquet'
    )
    TO 'cleaned.parquet'
    (FORMAT PARQUET);
""")



