import duckdb

duckdb.sql("""
COPY(
    SELECT DISTINCT
    TRIM(session_id) AS session_id,
    session_date,
    customer_id,
    store_id,
    device_type,
    SPLIT_PART(TRIM(browser, ,os) AS browser


    
    ))


