# geographic
This repository compiles scripts I have written to faciliate the processing and analysis of data broken down by geographic location (state, county, etc.).

The states.sh script is a bash-language script that is intended to be run from the command line, and its function is to convert the two-letter abbreviations for each US state (as well as the District of Columbia) into the state/district's full name. It should be run by entering "./states.sh filename", where you want to replace all the two-letter US state abbreviations in the file "filename" with their full names, and where said file is in the current directory.

The COVID-data-nyt.py script is a Python-language script that is also intended to be run from the command line. It is specifically intended to be run on the NYT COVID-19 county-level raw data page at their GitHub repository, which can be found at this URL: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv In other words, it is run from the command line by executing the following command: "python COVID-data-nyt.py 'date'", where the word "date" is replaced with the actual date for which you want to extract the county-level data, formatted in YYYY-MM-DD format (but the single quotation marks should be retained). For instance, to extract only data from June 12, 2020 from the NYT's county-level dataset, you would run the following from command line:

  python COVID-data-nyt.py '2020-06-12'
  
Using the COVID-data-nyt.py results in the production of the file new.txt in the current directory, which contains all of the NYT's data for the desired date.
