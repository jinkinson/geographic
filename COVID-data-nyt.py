import os
import sys
import requests
url='https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
myfile=requests.get(url)
open('/Users/jinkinsonsmith/Documents/Scripting/us-counties.csv','wb').write(myfile.content)
file=open('us-counties.csv')
lines=file.readlines()
data=[]
for i in range(len(lines)):
    lines[i]=lines[i].split(',')
    if(lines[i][0]==sys.argv[1]):
        data.append(lines[i])
with open('new.txt','w') as f:
    for i in range(len(data)):
        f.writelines(",".join(str(x) for x in data[i]))
#This replaces the contents of the file new.txt with all the COVID-19 data for the desired date, shown here as 2020-06-06.
#Also, each line in the output file new.txt contains all six fields, separated by commas, as the original NYT dataset:
#Date, County, State, fips, cases, deaths
