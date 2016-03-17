#!/usr/bin/make
# 
all: test

lint:
			pylint ./template-fbi-ucr.py > pylint1.txt
test: 
			python ./template-fbi-ucr.py > ./fbi-ucr.py
			pylint ./fbi_ucr.py > pylint2.txt 
			python ./fbi-ucr.py CrimeStatebyStateAll.csv > ./result.csv

clean: 
			rm -f ./fbi-ucr.py
			rm -f ./result.csv
			ls -l
