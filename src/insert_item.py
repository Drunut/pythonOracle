#!/usr/bin/python


import sys, cx_Oracle
sys.path.append("\dataPython\oracle\lib")

try:
	dsnVar = cx_Oracle.makedsn('Tantalum', '1521')
	db = cx_Oracle.connect(user='student', password='student', dsn=dsnVar)

	#Create our cursor so I can use it with the database
	cursor = db.cursor()

	#Make an insert statement, execute, and commit the change
	stmt = "INSERT INTO item VALUES (item_s1.nextval, '12345678909876', 1011, 'This is My New Video', 'Now With a Subtitle', 'PG-13', TO_DATE('November 16, 2017', 'MONTH DD, YYYY') , 1, TO_DATE('November 16, 2017', 'MONTH DD, YYYY'), 1, TO_DATE('November 16, 2017', 'MONTH DD, YYYY'))"
	cursor.execute(stmt)
	db.commit()

except cx_Oracle.DatabaseError, e:
	error, = e.args
	print >> sys.stderr, "Oracle-Error-Code:", error.code
	print >> sys.stderr, "Oracle-Error-Message:", error.message

cursor.close()
db.close()