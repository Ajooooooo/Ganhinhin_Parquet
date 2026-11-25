import duckdb

duckdb.sql("""
COPY(
    SELECT DISTINCT
    TRIM(session)
    
    ))


