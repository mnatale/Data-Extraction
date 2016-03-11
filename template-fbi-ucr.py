print("#!/usr/bin/python \n\
\n\
################################################################################\n\
# Requires Python 3.x or later\n\
# The following code is a brut force method to xtract strings from the output\n\
# of a text file. Once extracted the strings are scrubbed and # formated for \n\
# Excel or Tableau processing.\n\
#\n\
# Author: Mark Natale - Boston MA\n\
# email: mnatalex54@gmail.com\n\
#\n\
# Copyright 2016\n\
#\n\
# Orignal work\n\
# Revision: 0.2 \n\
################################################################################\n\
\n\
# Py Library Imports\n\
import re\n\
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
	finname = sys.argv[1]\n\
else:\n\
	sys.exit(\"File name required. Exit\")\n\
\n\
fhobj = open(finname, \"r\")\n\
")

print("\n\
##############################################################################\n\
# Insert header from data table here to auto-gen custom file.\n\
")
header_str = "Year,Population,Violent crime total,Murder and nonnegligent Manslaughter,Forcible rape,Robbery,Aggravated assault,Property crime total,Burglary,Larceny-theft,Motor vehicle theft,Violent Crime rate,Murder and nonnegligent manslaughter rate,Forcible rape rate,Robbery rate,Aggravated assault rate,Property crime rate,Burglary rate,Larceny-theft rate,Motor vehicle theft rate"

prepend_header = "print (\"State\",\"\\t\",\""

append_header = "\")"
new_header = ""
for i in header_str.replace(",", "\",\"\\t\",\""):
    new_header = new_header + i
print(prepend_header + new_header + append_header)

print("\n\
\n\
\n\
##############################################################################\n\
# Main line processing loop.\n\
while True:\n\
	line = fhobj.readline()\n\
	if len(line) > 400:\n\
		print(len(line))\n\
		sys.exit(\"Readline error: Line length is longer than expected. \")\n\
\n\
	if len(line) == 0:	# Check for zero length line as EOF and exit loop\n\
		break\n\
\n\
	line_list = line.rstrip().replace(\",\", \" \").split()	# remove commas, clean ws\n\
\n\
	if line_list == '\\n':    # bypass empty lines\n\
		continue\n\
	if line_list == []:\n\
		continue\n\
\n\
\n\
##############################################################################\n\
")

print("\n\
	# Isolate  line containing State. Join two word state names and WDC.\n\
	if line_list[0] ==\"Estimated\":\n\
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

################################################################################
# Assemble the data reference to dictonary name string
#
################################################################################
append_list = "'] = line_list[%d]"
new_list = "\tdlist['"
for i in header_str.replace(",", "'] = line_list[%d]\n\tdlist['"):
    new_list = new_list + i
new_list = new_list + append_list

# Now that the 'dlist' string is fully assembled, need to place the line_list
# index values in the string.
num = 0
for x in new_list:
    new_list = new_list.replace("%d", str(num), 1)
    num += 1

new_list = new_list.replace("dlist['Year']  = line_list",
                            "dlist['Year'] = \"1/31/\" + line_list")

print(new_list)

print("\n\
##############################################################################\n\
# Gen the data vectors for output\n\
")

prepend_list = "\tprint (dlist['STATE'],\"\\t\","
append_dlist = "'])"
print_list = "dlist['"
for i in header_str.replace(",", "'], \"\\t\", dlist['"):
    print_list = print_list + i
print_list = print_list + append_dlist
print(prepend_list + print_list)

print("\n\
fhobj.close()\n\
")

