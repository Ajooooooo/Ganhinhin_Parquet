import duckdb

duckdb.sql("""
    COPY(
        SELECT DISTINCT 
    (FORMAT PARQUET);
""")


