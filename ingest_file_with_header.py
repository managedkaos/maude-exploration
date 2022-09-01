'''
Exploring MAUDE
- This function is for processing the MDR data
'''
import pandas as pd
import sqlite3

df = pd.read_csv('./mdrfoi_HEAD.txt', sep="|")
db = sqlite3.connect("./database/mdrfoi.sqlite")

print(df.keys())

# Write the new DataFrame to a new SQLite table
df.to_sql("mdrfoi", db, if_exists="replace")

db.close()
