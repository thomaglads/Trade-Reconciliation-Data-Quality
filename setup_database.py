
import sqlite3
import pandas as pd

# --- Configuration ---
DB_NAME = 'trades.db'
FO_CSV = 'front_office_trades.csv'
BO_CSV = 'back_office_trades.csv'

# --- Read CSV files ---
fo_df = pd.read_csv(FO_CSV)
bo_df = pd.read_csv(BO_CSV)

# --- Connect to SQLite and write data ---
conn = sqlite3.connect(DB_NAME)

fo_df.to_sql('front_office', conn, if_exists='replace', index=False)
bo_df.to_sql('back_office', conn, if_exists='replace', index=False)

conn.close()

print(f"Successfully created database '{DB_NAME}' and imported data.")
