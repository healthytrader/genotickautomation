import random
import sys
import MySQLdb
import time
import numpy
stock=sys.argv[1]
db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()

mysymbol = sys.argv[1]
cursor.execute("select lastdate from lastdate where symbol = '"+mysymbol+"'")
mydata = cursor.fetchone();
mylastdate = str(mydata[0])
mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate >= '"+mylastdate+"' order by quotedate limit 66"
cursor.execute(mysql)
mydata = cursor.fetchall();
myfirstdate = str(mydata[-1][0])
mylastdate = myfirstdate
mysql = "select quotedate from stockquotes where symbol = 'SPY' and quotedate < '"+mylastdate+"' order by quotedate desc limit 666"
cursor.execute(mysql)
mydata = cursor.fetchall();
myfirstdate = str(mydata[-1][0])
mysymbol = mysymbol[0:-1]
mysql = "select quotedate,close from stockquotes where symbol = '"+mysymbol+"' and quotedate < '"+mylastdate+"' and quotedate > '"+myfirstdate+"' order by quotedate"
cursor.execute(mysql)
mydata = cursor.fetchall()
for myrow in mydata:
	mys = str(myrow[0]).replace("-","")+","+str(myrow[1])
	print mys
