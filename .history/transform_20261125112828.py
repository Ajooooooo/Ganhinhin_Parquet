import duckdb

duckdb.sql("""
    COPY(
        SELECT DISTINCt
    (FORMAT PARQUET);
""")


