import duckdb

duckdb.sql("""
    COPY(
        SELECT DISTINCT name
    (FORMAT PARQUET);
""")


