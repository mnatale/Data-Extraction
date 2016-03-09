#!/usr/bin/make
# 
all: test

test: 
			python ./template-fbi-ucr.py > ./fbi-ucr.py
			python ./fbi-ucr.py CrimeStatebyStateAll.csv > ./result.csv
clean: 
			rm -f ./fbi-ucr.py
			rm -f ./result.csv
			ls -l
