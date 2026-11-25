import duckdb

duckdb.sql("""
    COPY(
    SELECR * 
    FROM website_sessions)
)