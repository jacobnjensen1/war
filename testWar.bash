#!/bin/bash

rm warOutput.txt
rm warTrends.csv

./setup.py
for i in {1..2000}
do
	./war.py >> warOutput.txt
	./checkWar.py
done

Rscript plotTrends.R
