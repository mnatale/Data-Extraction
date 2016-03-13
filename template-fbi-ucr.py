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
print("#!/usr/bin/python\n\
# Auto-generated Pyhthon codei\n\
# Requires Python 3.x or later\n\
# The following code is a brut force method to xtract strings from the output\n\
# of a text file. Once extracted the strings are scrubbed and # formated for\n\
# Excel or Tableau processing.\n\
#\n\
# Author: Mark Natale - Boston MA\n\
# email: mnatalex54@gmail.com\n\
#\n\
# Copyright 2016\n\
#\n\
# Orignal work\n\
# Revision: 0.2\n\
\n\
# Py Library Imports\n\
import sys\n\
\n\
# Local imports\n\
# None\n\
\n\
# Global var init\n\
dlist = {}\n\
\n\
# Get the file name from argv[1] and open file handle.\n\
if len(sys.argv) > 1:\n\
    file_name = sys.argv[1]\n\
else:\n\
    sys.exit(\"File name required. Exit\")\n\
\n\
fhobj = open(file_name, \"r\")\n\
")

print("\n\
# Header from row 1 of data table.\n\
")

# Insert comma separated header here
header_str = "Year,Population,Violent crime total,Murder and nonnegligent Manslaughter,Forcible rape,Robbery,Aggravated assault,Property crime total,Burglary,Larceny-theft,Motor vehicle theft,Violent Crime rate,Murder and nonnegligent manslaughter rate,Forcible rape rate,Robbery rate,Aggravated assault rate,Property crime rate,Burglary rate,Larceny-theft rate,Motor vehicle theft rate"

prepend_header = "print(\"State\", \",\", \""
append_header = "\", sep='')"
new_header = ""

for i in header_str.replace(",", "\", \",\", \""):
    new_header = new_header + i

# Gen fully formed header
print(prepend_header + new_header + append_header)

print("\n\
\n\
# Main line processing loop.\n\
while True:\n\
    line = fhobj.readline()\n\
    if len(line) > 400:\n\
        print(len(line))\n\
        sys.exit(\"Readline error: Line length is longer than expected.\")\n\
\n\
    if len(line) == 0:	# Check for zero length line as EOF and exit loop\n\
        break\n\
\n\
    line_list = line.rstrip().replace(\",\", \" \").split()	# remove ',' and ws\n\
\n\
    if line_list == '\\n':    # bypass empty lines\n\
        continue\n\
    if line_list == []:\n\
        continue\n\
\n\
")

print("\n\
	# Isolate  line containing State. Join two word state names and WDC.\n\
    if line_list[0] == \"Estimated\":\n\
\n\
        if line_list[3] == \"NEW\":\n\
            dlist['STATE'] = line_list[3] + \" \" +  line_list[4]\n\
        elif line_list[3] == \"North\":\n\
            dlist['STATE'] = line_list[3] + \" \" +  line_list[4]\n\
        elif line_list[3] == \"South\":\n\
            dlist['STATE'] = line_list[3] + \" \" +  line_list[4]\n\
        elif line_list[3] == \"West\":\n\
            dlist['STATE'] = line_list[3] + \" \" +  line_list[4]\n\
        elif line_list[3] == \"District\":\n\
            dlist['STATE'] = line_list[3] + \" \" +  line_list[4] + \" \" +  line_list[5]\n\
        else:\n\
            dlist['STATE'] = line_list[3]\n\
        continue\n\
\n\
    # Exclude repeating data headers\n\
    if line_list[0] == \"Year\":\n\
        continue\n\
")

# Assemble the data reference to dictonary name string
new_list = "    dlist['"
append_list = "'] = line_list[%d]"

for i in header_str.replace(",", "'] = line_list[%d]\n    dlist['"):
    new_list = new_list + i

new_list = new_list + append_list

# Now that the 'dlist' string is fully assembled, need to place the line_list
# index values in the string.
num = 0
for x in new_list:
    new_list = new_list.replace("%d", str(num), 1)
    num += 1

new_list = new_list.replace("dlist['Year'] = line_list",
                            "dlist['Year'] = \"12/31/\" + line_list")

print(new_list)

print("\n\
##############################################################################\n\
# Gen the data vectors for output\n\
")

prepend_list = "    print(dlist['STATE'], \",\", "
append_dlist = "'], sep='')"
print_list = "dlist['"

for i in header_str.replace(",", "'], \",\", dlist['"):
    print_list = print_list + i

print_list = print_list + append_dlist

print(prepend_list + print_list)

print("\n\
fhobj.close()\n\
")

