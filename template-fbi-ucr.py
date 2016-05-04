"""
Requires: Python 3.x or later

    Author: Mark Natale - Boston MA
    email: mnatalex54@gmail.com
    Copyright 2016
    https://github.com/mnatale/Data-Extraction

This program is a template that generates a formatted python program based on
column names of the header row of data file. The source data file in this
example is keyed on US state names including WDC and a 4 digit year. The
template reads the data file state-by-state and assembles a row/col
format with State, fully formed date and corresponding data.

    Raw data in format:
      Estimated crime in Alabama,,,,,,,,,,,,,,,,,,,
      ,,,,,,,,,,,,,,,,,,,
      Year,Population,Violent crime total,Murder and Manslaughter,...
      1960,3266740,6097,406,281,...
      1961,3302000,5564,427,252,...
      ...

    Generated output format:
      State,Year,Population,Violent crime total,Murder and Manslaughter,...
      Alabama,12/31/1960,3266740,6097,406,281,...
      Alabama,12/31/1961,3302000,5564,427,252,...
      ...

Usage: Python template-fbi-ucr.py > fbi-ucr.py

"""

# Template begins here
print("""#!/usr/bin/python
# Auto-generated Python code
# Requires Python 3.x or later
# The following code is a brut force method to xtract strings from the output
# of a text file. Once extracted the strings are scrubbed and # formated for
# Excel or Tableau processing.
#
# Author: Mark Natale - Boston MA
# email: mnatalex54@gmail.com
#
# Copyright 2016
#
# Py Library Imports
import sys
import argparse

# Global var init
dlist = {}

def openfile():
    parser = argparse.ArgumentParser(description='Process comma separated text file.')
    parser.add_argument('filename')
    args = parser.parse_args()
    return open(args.filename, "r")

def main(fhobj):
# Header from row 1 of data table.
""")

# Insert comma separated header here
header_str = "Year,Population,Violent crime total,Murder and nonnegligent Manslaughter,Forcible rape,Robbery,Aggravated assault,Property crime total,Burglary,Larceny-theft,Motor vehicle theft,Violent Crime rate,Murder and nonnegligent manslaughter rate,Forcible rape rate,Robbery rate,Aggravated assault rate,Property crime rate,Burglary rate,Larceny-theft rate,Motor vehicle theft rate"

prepend_header = "    print(\"State\", \",\", \""
append_header = "\", sep='')"
new_header = ""

for i in header_str.replace(",", "\", \",\", \""):
    new_header = new_header + i

# Gen fully formed header for 1st row
print(prepend_header + new_header + append_header)

print("""
# Main line processing loop.
    for line in fhobj:
        if len(line) > 400:
            print(len(line))
            sys.exit("Readline error: Line length is longer than expected.")
				# split the comma separate line into a vector
        line_content = line.rstrip().replace(",", " ").split()    # remove ',' and ws

        # Filter out unnwanted lines
        if line_content == '':    # filter blank lines
            continue
        if line_content == []:    #Filter out line full of nulls(,,,,,)
            continue
        if line_content[0] == "Year":
            continue

        # Isolate  lines containing State. Join two word state names and WDC.
        if line_content[0] == "Estimated":
            if line_content[3] == "NEW":
                dlist['STATE'] = line_content[3] + " " +  line_content[4]
            elif line_content[3] == "North":
                dlist['STATE'] = line_content[3] + " " +  line_content[4]
            elif line_content[3] == "South":
                dlist['STATE'] = line_content[3] + " " +  line_content[4]
            elif line_content[3] == "West":
                dlist['STATE'] = line_content[3] + " " +  line_content[4]
            elif line_content[3] == "District":
                dlist['STATE'] = line_content[3] + " " +  line_content[4] + " " +  line_content[5]
            else:
                dlist['STATE'] = line_content[3]
            continue
						""")

# Assemble the data reference to dictonary name string.
# Keep 8 spaces prepended to dlist
new_list = "        dlist['"
append_list = "'] = line_content[%d]"

for i in header_str.replace(",", "'] = line_content[%d]\n        dlist['"):
    new_list = new_list + i

new_list = new_list + append_list

# Now that the 'dlist' string is fully assembled, need to place the line_content
# index values in the string.
num = 0
for x in new_list:
    new_list = new_list.replace("%d", str(num), 1)
    num += 1

new_list = new_list.replace("dlist['Year'] = line_content",
                            "dlist['Year'] = \"12/31/\" + line_content")

print(new_list)

print("""
# Gen the data for output
""")

prepend_list = "        print(dlist['STATE'], \",\", "
append_dlist = "'], sep='')"
print_list = "dlist['"

for i in header_str.replace(",", "'], \",\", dlist['"):
    print_list = print_list + i

print_list = print_list + append_dlist

print(prepend_list + print_list)

print("""
if __name__ == "__main__":
    main(openfile())
""")

