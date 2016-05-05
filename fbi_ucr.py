#!/usr/bin/python

"""
The following code extracts data line by line from a text file and 
output can be used by Excel, Tableau or other BI tools for processing.

Requires Python 3.x or later.
Author: Mark Natale - Boston MA
email: mnatalex54@gmail.com
Copyright 2016
"""
# Library Imports
import sys
import argparse

def openfile():
    """Input Parsing."""
    parser = argparse.ArgumentParser(description='Process comma separated text file.')
    parser.add_argument('filename')
    args = parser.parse_args()
    return open(args.filename, "r")

def format_data(fhobj):
    """All the work gets done here."""
    dlist = {}
    first_pass = False
    # Main line processing loop.
    for line in fhobj:
        if len(line) > 400:
            print(len(line))
            sys.exit("Readline error: Line length is longer than expected.")
        # split the comma separate line into a vector
        line_content = line.rstrip().replace(",", " ").split()

        # Filter out unwanted lines
        if line_content == '':    # filter blank lines
            continue
        if line_content == []:    #Filter out line full of nulls(,,,,,)
            continue

        # Check for header row by looking up first column name
        # can't assume row 1 so lookup by 1st two colnames
        if line_content[0] == "Year":
            if first_pass == True:
                continue
            first_pass = True
            header_st = "State," + line.rstrip('\n')
            header_str = line.rstrip('\n')
            print(header_st, end='\n')
            continue

        # Isolate lines containing State names.
        if line_content[0] == "Estimated":
            dlist['State'] = str(line_content[3:]) \
                .strip('[]').replace(",", "").replace("'", "")
            continue

        # Populate hash
        for colname, val in zip(header_str.split(','), line_content):
            if colname != "Year":
                dlist[colname] = val
            else:
                dlist[colname] = "12/31/" + val

        # Align hash data with header layout for output
        new_line = []
        for colname in header_st.split(','):
            new_line.append([v for (k, v) in dlist.items() if k == colname])
        new_line = str(new_line).replace('[', '').replace(']', '')
        print(new_line.replace("'", ""))

# main
if __name__ == "__main__":
    format_data(openfile())

