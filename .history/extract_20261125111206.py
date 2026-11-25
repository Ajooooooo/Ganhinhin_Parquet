import duckdb

duckdb.sql("""
    COPY(
    S   ELECT * 
    FROM read_csv_auto('website_sessions.csv')
    )
    TO 'extract.parquet'
    (FORMAT PARQUET);
""")


