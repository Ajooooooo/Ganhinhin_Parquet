import duckdb

duckdb.sql("""
    COPY(
    SELECR * 
    FROM read_csv_auto('website_sessions.csv')
)
TO 'extract.parquet'


import duckdb

duckdb.sql("""
    COPY (
        SELECT *
        FROM read_csv_auto('website_sessions.csv')
    )
    TO 'bronze_website_session.parquet'
    (FORMAT PARQUET);
""")
