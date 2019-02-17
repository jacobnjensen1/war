#!/bin/bash

rm warOutput.txt
rm warTrends.csv

./setup.py
for i in {1..200}
do
	echo "" > warOutput.txt
	for j in {1..10}
	do
		./war.py >> warOutput.txt
	done
	./checkWar.py
done

Rscript plotTrends.R
