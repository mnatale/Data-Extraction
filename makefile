#!/usr/bin/make
# 
all: test

lint1:
			pylint ./template-fbi-ucr.py

lint2:
			pylint ./fbi-ucr.py

test: 
			python ./template-fbi-ucr.py > ./fbi-ucr.py
			python ./fbi-ucr.py CrimeStatebyStateAll.csv > ./result.csv

clean: 
			rm -f ./fbi-ucr.py
			rm -f ./result.csv
			ls -l
