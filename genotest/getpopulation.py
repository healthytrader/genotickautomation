import random
import sys
import MySQLdb
import time
import numpy

db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()
tablename = "genosum"
symbol = sys.argv[2]
mysql = "select lastdate from lastdate where symbol = '"+symbol+"'"
cursor.execute(mysql)
mdata = cursor.fetchone()
mylastdate = str(mdata[0])
mysql  = "select population from "+tablename+"  where symbol = '"+symbol+"' and lastdate = '"+mylastdate+"' and  myreturn > 0 and mymedian > 0 and myavg > 0 order by mymedian desc limit 7"
#mysql  = "select population from "+tablename+"  limit 7"
cursor.execute(mysql)
mydata = cursor.fetchall()
myrow = int (sys.argv[1]) - 1
mypopulation = mydata[myrow][0]
print mypopulation.split("-")[2].split(".")[0]
