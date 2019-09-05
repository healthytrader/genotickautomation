import random
import sys
import MySQLdb
import time
import numpy
db = MySQLdb.connect("127.0.0.1","genotick","mypassword","genotick" )
cursor = db.cursor()
mysymbol = sys.argv[1]
mysql = "select lastdate from lastdate where symbol = '"+mysymbol+"'"
cursor.execute(mysql)
data = cursor.fetchone()
mylastdate = str(data[0])
print mylastdate
mysql = "delete from genosum where symbol = '"+mysymbol+"' and lastdate = '"+mylastdate+"'"
cursor.execute(mysql)
db.commit()
import glob, os
for file in glob.glob("ge*.txt"):
	try:
	    	print(file)
		runningpnl=[]
		profit=[]
		res2=0
		with open(file) as f:
    			content = f.readlines()
		# you may also want to remove whitespace characters like `\n` at the end of each line
		content = [x.strip() for x in content] 
	
		for myx in content:
			if "Closing data" in myx and "profit" in myx and "reverse" not in myx:
				ish = float(myx.split(" ")[4][0:-1])
				prof= float(myx.split(" ")[8][0:-1])
				if ish<0:
					ish=ish*-1	
					prof = prof * -1
				myprof = prof / ish
				res2 = res2 + prof
				runningpnl.append(res2)		
				profit.append(myprof)
		mynum = numpy.array(profit)
       	 	mymedian = numpy.median(mynum)
	        myavg = numpy.average(mynum)
		print file,mymedian,myavg,runningpnl[-1]
		mysql = "insert into genosum (population,mymedian,myavg,myreturn,symbol,lastdate) values ('"+str(file)+"',"+str(mymedian)+","+str(myavg)+","+str(runningpnl[-1])+",'"+mysymbol+"','"+mylastdate+"')"
		print mysql	
		cursor.execute(mysql)
		db.commit()
	except:
		pass
