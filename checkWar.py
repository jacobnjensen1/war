#!/usr/bin/python3
import csv

iFilename = "warOutput.txt"
oFilename = "warTrends.csv"

iFile = open(iFilename, 'rt')
lines = iFile.readlines()

#outFile needs to be opened twice, as r and as a

oneWins = 0
twoWins = 0

with open(oFilename, 'rt') as previous:
	lastResult = previous.readlines()[-1].strip().split(',')

	oneWins = int(lastResult[0])
	twoWins = int(lastResult[1])

	for line in lines:
		if "One" in line:
			twoWins += 1
		elif "Two" in line:
			oneWins += 1
		elif "oops" in line:
			raise ValueError("Failed match")
		else:
			continue
	previous.close()

outFile = open(oFilename, 'at')
results = csv.writer(outFile, delimiter=',')
results.writerow([oneWins] + [twoWins])

outFile.close()
iFile.close()
