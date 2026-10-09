# data.duckdb
> One-Click Database of All CARTA's Open Data 
<img width="467" height="193" alt="image" src="https://github.com/user-attachments/assets/f1e0e671-dad1-4292-a3a4-a5ab38db1e39" />

## Try it Out
You can quickly start querying the data by clicking [here](https://shell.duckdb.org/#queries=v0,ATTACH-'https%3A%2F%2Fgocarta.s3.us%20east%202.amazonaws.com%2Fpublic%2Fduckdb%2Fdata.duckdb'-as-data~,SELECT-*-FROM-duckdb_views()-WHERE-NOT-internal~,SELECT-*-FROM-data.gtfsrt_vehicle_positions_v1-LIMIT-5~)

## Import
You can add this database into your own DuckDB instance with one line by using DuckDB's attach mechanism:
```
ATTACH 'https://gocarta.s3.us-east-2.amazonaws.com/public/duckdb/data.duckdb' as data;
```

## Background
Both data availability and access are important.  CARTA publishes all its open datasets using [datablob](https://pypi.org/project/datablob) in numerous file formats, including parquet.  After making data available, we wanted to drive down the friction in accessing and analyzing the data, so we created data.duckdb.  A single DuckDB database that points to all our open datasets.  It enables people to easily query, filter, and join all our open datasets.

## Example
Here's an example of using data.duckdb to query across multiple tables.  In this example we get all the Bike Chattanooga stations within 25 meters of Route 4.  
<img width="428" height="292" alt="image" src="https://github.com/user-attachments/assets/93371098-fdee-4381-ae78-43d1628c9963" />

## Download
You can directly download the database here:  
https://gocarta.s3.us-east-2.amazonaws.com/public/duckdb/data.duckdb
