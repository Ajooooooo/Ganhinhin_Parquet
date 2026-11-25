import duckdb

duckdb.sql("""
    COPY(
    SELECR * 
    FROM read_csv_auto('website_sessions.csv')
)
TO 'Ganhinhin.par'