#!/usr/bin/env python
"""Process a parquet file and output its records in key=value format"""
import argparse
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_parquet.html#pandas.read_parquet
import pandas as pd

parser = argparse.ArgumentParser(add_help=True, prog="preader.py")
parser.add_argument("pfile", type=str, nargs=1, help="parquet file to process")
args = parser.parse_args()

# create object containing records from the parquet file (can specify fields)
# table = pd.read_parquet(args.pfile[0], columns=['registration_dttm', 'first_name', 'last_name', 'email'])
table = pd.read_parquet(args.pfile[0])

# convert the parquet data to an iterable object
tdict = table.to_dict('index')

# process converted parquet file to output as key=value pairs for Splunk
def main():
    for rec in tdict.iteritems():
        print 'record_num='+str(rec[0]),
        for key,value in rec[1].iteritems():
            print key+'='+'"'+str(value)+'"',
        print '\n',


if __name__ == "__main__":
    main()
