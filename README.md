# Data-Extraction

## Lint
[![Code Health](https://landscape.io/github/mnatale/Data-Extraction/master/landscape.svg?style=plastic)](https://landscape.io/github/mnatale/Data-Extraction/master)

## Build
[![Build Status](https://travis-ci.org/mnatale/Data-Extraction.svg?branch=master)](https://travis-ci.org/mnatale/Data-Extraction)
[![Requirements Status](https://requires.io/github/mnatale/Data-Extraction/requirements.svg?branch=master)](https://requires.io/github/mnatale/Data-Extraction/requirements/?branch=master)
## Code Coverage
[![Coverage Status](https://coveralls.io/repos/github/mnatale/Data-Extraction/badge.svg?branch=master)](https://coveralls.io/github/mnatale/Data-Extraction?branch=master)

###Description
The source data file in this example is keyed on US state names including Washington DC and a 4-digit year (%Y). The template reads the data file state-by-state and assembles a row/col
format with State, fully formed date (%m/%d/%Y) and corresponding data. BI applications behave better with fully formed dates.

    Raw data input format from source file:
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

### Running Auto-generated Script
**Usage:** python fbi-ucr.py > &lt;formatted-file-name&gt;.csv

**Source Data**
    <p>The source data files used for this example is from FBI, Uniform Crime Reports, prepared by the National Archive of Criminal Justice Data Date of download: Mar 22 2015 http://www.ucrdatatool.gov</p>

###To-do list
- [x] re-write with functions.
- [ ] Automated data extraction and from website.
- [X] Automated year concatenation.
- [X] Rewrite code to do all text processing - no template
- [ ] Write output to .csv file
