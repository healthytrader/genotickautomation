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
mysql = "select lastdate from lastdate where symbol = '"+stock+"'"
cursor.execute(mysql)
datearray=cursor.fetchone()

mypopulation=sys.argv[1]

print "population",mypopulation
f = open(inputfile,'w')
f.write("dataDirectory data\r\n")

f.write("startTimePoint	"+datearray[0].replace("-","")+"\r\n")
f.write("endTimePoint	\r\n")
f.write("populationDAO	savedPopulation_"+mypopulation+"\r\n")
f.write("performTraining false\r\n")
f.close()
