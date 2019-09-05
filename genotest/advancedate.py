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
nextlastdate = str(mydata[-1][0])
print nextlastdate
mysql = "update lastdate set lastdate = '"+nextlastdate+"' where symbol = '"+stock+"'"
print mysql
cursor.execute(mysql)
db.commit()
