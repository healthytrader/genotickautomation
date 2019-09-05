import random
import sys
import MySQLdb
import time
import numpy

db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()


def gettradingday (startdate):
	startdate = startdate[0:4]+"-"+startdate[4:6]+"-"+startdate[6:8]
	mysql = "select quotedate from stockquotes where symbol = 'spy' and quotedate > '"+startdate+"' order by quotedate limit 1"
	cursor.execute(mysql)
	data = cursor.fetchone()
	return str(data[0])

import glob, os
outputfile="output.txt"
population = sys.argv[1]
symbol = sys.argv[2]
with open(outputfile) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
for myline in content:
	if "next trade" in myline and "reverse" not in myline:
		mydate =str( myline.split(" ")[3])
		mydir = str(myline.split(" ")[8])
		print mydate,"for next day",mydir,population
		nextday = gettradingday(mydate)
		mysql = "insert into votes (votedate,tradeentry,direction,population,symbol) values ('"+mydate+"','"+nextday+"','"+mydir+"','"+population+"','"+symbol+"')"
		cursor.execute(mysql)
		db.commit()
