#!/usr/bin/make
# 
all: test

lint1:
			pylint ./fbi_ucr.py

test: 
			python ./fbi_ucr.py CrimeStatebyStateAll.csv > data.txt


clean: 
			rm -f ./data.txt
			ls -l
