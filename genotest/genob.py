import random
import sys
import MySQLdb
import time
import numpy

db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()
stock=sys.argv[1]
import glob, os
outputfile="output.txt"

with open(outputfile) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
mydate=""
mydir = ""
for myline in content:

	if "next trade" in myline and "reverse" not in myline:
		mydate =str( myline.split(" ")[3])
		mydir = str(myline.split(" ")[8])
myd = mydate
mydate = myd[0:4]+"-"+myd[4:6]+"-"+myd[6:]
mysql = "select quotedate,close from stockquotes where symbol = '"+stock+"' and quotedate > '"+mydate+"' order by quotedate limit 2"
cursor.execute(mysql)
mydata = cursor.fetchall()
myentrydate = str(mydata[0][0])
myentryval = float(mydata[0][1])
myexitdate = str(mydata[1][0])
myexitval = float(mydata[1][1])
profit=0
if mydir=="DOWN":
	ish = int(10000/myentryval)
	price1 = myentryval - myexitval
	price1 = ish * price1
elif mydir=="UP":
	ish = int(10000/myentryval)
        price1 = myexitval-myentryval
        price1 = ish * price1
print myentrydate+","+str(price1)+","+str(ish)
