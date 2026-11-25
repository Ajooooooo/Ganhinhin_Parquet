import duckdb

duckdb.sql("""
    COPY(
        SELECT 
    (FORMAT PARQUET);
""")

