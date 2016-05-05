#!/usr/bin/make
# 
all: test

lint1:
			pylint ./template-fbi-ucr.py

test: 
			python ./template-fbi-ucr.py CrimeStatebyStateAll.csv > data.txt


clean: 
			rm -f ./data.txt
			ls -l
