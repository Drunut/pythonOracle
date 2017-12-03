#!/usr/bin/python


import sys, cx_Oracle
sys.path.append("\dataPython\oracle\lib")

dsnVar = cx_Oracle.makedsn('Tantalum', '1521')
db = cx_Oracle.connect(user='student', password='student', dsn=dsnVar)

#Create our cursor so I can use it with the database
cursor = db.cursor()

#Make a SELECT statement
stmt = "SELECT * FROM item"



#Execute it using the cursor
cursor.execute(stmt)

#Print 'em
for row in cursor:
	for column, i in zip(cursor.description, range(0, len(row)) ):
		spaces = " "*(24 - len(column[0]))
		print column[0]+spaces+str(row[i])

cursor.close()
db.close()