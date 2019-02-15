#!/usr/bin/python3

import csv

oFilename = "warTrends.csv"

with open(oFilename, 'w') as csvOut:
	writeTo = csv.writer(csvOut)
	writeTo.writerow(["one"] + ["two"])

csvOut.close()
