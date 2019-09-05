import random
import sys
import MySQLdb
import time
import numpy

db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()

def getnexttradingday (startdate):
	mysql = "select quotedate from stockquotes where symbol = 'spy' and quotedate > '"+startdate+"' order by quotedate limit 1"
	cursor.execute(mysql)
	data = cursor.fetchone()
	return str(data[0])

symbol = sys.argv[1]
mysql = "select distinct tradeentry from votes where symbol = '"+symbol+"'"
cursor.execute(mysql)
mydata = cursor.fetchall()
datelist=[]
for myrow in mydata:
	datelist.append(str(myrow[0]))
print datelist
for mydate in datelist:
	iup=0
	idown=0
	mysql = "select direction from votes where symbol = '"+symbol+"' and tradeentry = '"+mydate+"'"
	cursor.execute(mysql)
	data = cursor.fetchall()
	for myrow in data:
		if myrow[0]=="UP":
			iup+=1
		elif myrow[0]=="DOWN":
			idown+=1
	szDir  = ""
	if iup > idown:
		szDir="UP"
	else:
		szDir="DOWN"
	nexttradingday = getnexttradingday(mydate)
	symbol2=symbol[0:-1]
	mysql1 = "select open from stockquotes where symbol = '"+symbol2+"' and quotedate = '"+mydate+"'"
	mysql2 = "select open from stockquotes where symbol = '"+symbol2+"' and quotedate = '"+nexttradingday+"'"
	cursor.execute(mysql1)
	myo1 = cursor.fetchone()
	cursor.execute(mysql2)
	myo2 = cursor.fetchone()
	ddiff = float(myo2[0])-float(myo1[0])
	if szDir=="DOWN":
		ddiff = ddiff * -1
	mysql = "insert into genotrades (upvotes,downvotes,entrydate,profit,symbol) values ("+str(iup)+","+str(idown)+",'"+mydate+"',"+str(ddiff)+",'"+symbol2+"')"
	cursor.execute(mysql)
	db.commit()

