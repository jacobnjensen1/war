#!/usr/bin/python3

import csv

oFilename = "warTrends.csv"

with open(oFilename, 'w') as csvOut:
	writeTo = csv.writer(csvOut)
	writeTo.writerow(["one"] + ["two"])
	#so we know which column is which
	writeTo.writerow([0] + [0])
	#0s tell checkWar that no one has won before any matches

csvOut.close()
