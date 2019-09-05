import random
import sys
import MySQLdb
import time
import numpy

db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()

symbol = sys.argv[1]
mysql = "select profit from genotrades where symbol = '"+symbol+"' order by entrydate"
cursor.execute(mysql)
mydata = cursor.fetchall()
for myrow in mydata:
	print myrow[0]
