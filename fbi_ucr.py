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
import textwrap

def openfile():
    """Input Parsing."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        The source data file in this example is keyed on US state names 
        including Washington DC and a 4-digit year (%Y). This program
        reads the data file state-by-state and assembles a row/col format
        with State, fully formed date (%m/%d/%Y) and corresponding data. 
        BI applications behave better with fully formed dates.

          Raw data input format from source file:
            Estimated crime in Alabama,,,,,,,,,,,,,,,,,,,
            ,,,,,,,,,,,,,,,,,,,
            Year,Population,Violent crime total,Murder and Manslaughter,...
            1960,3266740,6097,406,281,...
            1961,3302000,5564,427,252,...
            ...

          Generated output format:
            State,Year,Population,Violent crime total,Murder and Manslaughter,..
            Alabama,12/31/1960,3266740,6097,406,281,...
            Alabama,12/31/1961,3302000,5564,427,252,...
            ...
      '''))
    parser.add_argument('-s', '--silent',
        action='store_false', 
        default='store_true',
        help='Silent mode - no screen output.')

    parser.add_argument('rdfile', type=argparse.FileType('r'),
        help='Input file name required (text or csv).')

    parser.add_argument('wrfile', nargs='?',type=argparse.FileType('w'),
        default='fbi_ucr.csv',
        help='Optional output file name. Default is fbi_ucr.csv.')

    args = parser.parse_args()
    return args

def format_data(args):
    """All the work gets done here."""
    dlist = {}
    first_pass = False
    # Main line processing loop.
    for line in args.rdfile:
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
            args.wrfile.write(header_st + '\n')
            if args.silent: print(header_st, end='\n')
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
        args.wrfile.write(new_line.replace("'", "") + "\n")
        if args.silent: print(new_line.replace("'", ""))

    #Close files
    args.wrfile.close()
    args.rdfile.close()

# main
if __name__ == "__main__":
    format_data(openfile())

#<EOF>
