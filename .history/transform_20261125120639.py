import duckdb

duckdb.sql("""
COPY(
    SELECT DISTINCT
        session_id,
        session_date,
        customer_id,
        store_id,
        device_type,
        SPLIT_PART(TRIM(browser_os), '|', 1) AS browser,
        SPLIT_PART(TRIM(browser_os), '|', 2) AS os,
        session_purchase_made,
        session_duration_minutes,
    session_pages_visited,
    COALESCE(session_quality avg(session_quality) over()) AS session_quality,
    From 'extract.parquet'
    ))



