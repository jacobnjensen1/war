#!/usr/bin/python3
import csv

iFilename = "warOutput.txt"
oFilename = "warTrends.csv"

iFile = open(iFilename, 'rt')
lines = iFile.readlines()

oneWins = 0
twoWins = 0

with open(oFilename, 'rt') as previous:
	lastResult = previous.readlines()[-1].strip().split(',')

	oneWins = int(lastResult[0])
	twoWins = int(lastResult[1])
	#these come from warTrends.csv

	for line in lines:
	#these come from warOutput
		if "One" in line:
			twoWins += 1
		elif "Two" in line:
			oneWins += 1
		elif "oops" in line:
			raise ValueError("Failed match")
			#oops is the output from war if neither deck has 52 cards
		else:
			continue
	previous.close()

outFile = open(oFilename, 'at')
results = csv.writer(outFile, delimiter=',')
results.writerow([oneWins] + [twoWins])

outFile.close()
iFile.close()
