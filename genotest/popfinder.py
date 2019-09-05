import random
import sys
import MySQLdb
import time
import numpy

db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()
mysql = "select distinct population from genosum1"
cursor.execute(mysql)
data = cursor.fetchall()
for myrow in data:
	print "./lookf2.ksh ",(myrow[0].split("-")[2]).split(".")[0], "EWZ"
