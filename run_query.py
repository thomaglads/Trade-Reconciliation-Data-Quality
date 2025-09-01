
import sqlite3
import pandas as pd

# --- Configuration ---
DB_NAME = 'trades.db'
QUERY_FILE = 'reconciliation_query.sql'
OUTPUT_CSV = 'reconciliation_breaks.csv'

# --- Read the SQL query ---
with open(QUERY_FILE, 'r') as f:
    query = f.read()

# --- Connect to DB and execute ---
conn = sqlite3.connect(DB_NAME)

# Execute the query and load results into a DataFrame
breaks_df = pd.read_sql_query(query, conn)

conn.close()

# --- Save results to CSV ---
breaks_df.to_csv(OUTPUT_CSV, index=False)

print(f"Successfully executed query and saved {len(breaks_df)} breaks to '{OUTPUT_CSV}'.")
