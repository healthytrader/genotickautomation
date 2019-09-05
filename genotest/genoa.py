import random
import sys
import MySQLdb
import time
import numpy

db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()

import glob, os
inputfile="input.txt"
datafile="data/xxx.csv"
try:
    os.remove(inputfile)
except OSError:
    pass

stock=sys.argv[2]

with open(datafile) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
myd = content[-1].split(",")[0]
myd=myd[0:4]+"-"+myd[4:6]+"-"+myd[6:]

mysql = "select quotedate,close from stockquotes where symbol = '"+stock+"' and quotedate > '"+myd+"' order by quotedate limit 1"
cursor.execute(mysql)
myrow = cursor.fetchone()

try:
    os.remove(datafile)
except OSError:
    pass

mydate = str(myrow[0]).replace("-","")
myval = str(myrow[1])
f = open(datafile, 'w')
for myx in content:
	f.write(myx+"\r\n")
f.write(mydate+","+myval+"\r\n")
f.close() 

mypopulation=sys.argv[1]
print "population",mypopulation
f = open(inputfile,'w')
f.write("dataDirectory data\r\n")

f.write("startTimePoint	"+mydate+"\r\n")
f.write("endTimePoint	\r\n")
f.write("populationDAO	savedPopulation_"+mypopulation+"\r\n")
f.write("performTraining false\r\n")
f.close()
