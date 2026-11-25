import duckdb

duckdb.sql("""
    COPY(
    SELECR * 
    FROM website)
)