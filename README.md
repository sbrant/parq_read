parq_read.py is a sample script to enumerate records from a parquet file. The script converts the fields to key=value pairs, per record, for easy ingestion into Splunk.

# Requirements:
## Pandas
http://pandas.pydata.org/pandas-docs/stable/

---

usage: parq_read.py [-h] pfile

positional arguments:
  pfile       parquet file to process

  optional arguments:
    -h, --help  show this help message and exit
