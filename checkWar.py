#!/usr/bin/python3
import csv

iFilename = "warOutput.txt"
oFilename = "warTrends.csv"

iFile = open(iFilename, 'rt')
lines = iFile.readlines()

oneWins = 0
twoWins = 0
totalWins = 0

for line in lines:
	if "One" in line:
		twoWins += 1
		totalWins += 1
	elif "Two" in line:
		oneWins += 1
		totalWins += 1
	elif "oops" in line:
		raise ValueError("Failed match")
	else:
		continue

oneProp = oneWins / totalWins
twoProp = twoWins / totalWins

with open(oFilename, 'at') as outFile:
	results = csv.writer(outFile, delimiter=',')
	results.writerow([oneProp] + [twoProp])

outFile.close()
iFile.close()
