#!/bin/bash

rm warOutput.txt
rm warTrends.csv
#clean the directory for new run

./setup.py
#this makes warTrends.csv, and writes the first 2 rows
for i in {1..50}
do
	echo "" > warOutput.txt
	#needs to be cleared so that matches are only counted once
	for j in {1..40}
	#this loop determines the resolution of the analysis
	do
		./war.py >> warOutput.txt
	done
	./checkWar.py
	#this updates warTrends.csv to show the current count of wins after j matches
done

Rscript plotTrends.R
#this uses warTrends.csv to save a plot jpg showing the win proportions
