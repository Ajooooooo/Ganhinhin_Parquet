import duckdb

duckdb.sql("""
    COPY(
    SELECR * 
    FROM read_csv_auto())
)