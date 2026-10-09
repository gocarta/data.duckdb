# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "duckdb>=1.5.6",
# ]
# ///
import csv
import os
import duckdb

db_file = "data.duckdb"

if os.path.exists(db_file):
    os.unlink(db_file)

conn = duckdb.connect(db_file)

with open("datasets.csv") as f:
    datasets = list(csv.DictReader(f))

statement = ""
for row in datasets:
    dataset_name = row["name"]
    # should check that dataset name is only a-z and _

    data_url = row["url"]

    statement += f"CREATE VIEW {dataset_name} AS SELECT * FROM '{data_url}';\n"

result = conn.execute(statement).fetchall()

conn.close()
