#!/usr/bin/python

# Import necessary libraries.
import sys, cx_Oracle

# Add to the environment Python path.
# Appending run-time path with a new location
sys.path.append("\dataPython\oracle\lib")

# Import local library module.
from strOracleVersion import formatVersion

# Use the HOST and PORT from:
# C:\oraclexe\app\oracle\product\11.2.0\server\network\ADMIN\tnsnames.ora
dsnVar = cx_Oracle.makedsn('Tantalum', '1521') #from tnsnames.ora
# Create a connection (there are shorter ways to format but in ther interest of verbosity...)
db = cx_Oracle.connect(user='student', password='student', dsn=dsnVar)

# Get the version of the database.
s = db.version
print s
# Call the library funcxtion to format the version.
print formatVersion(s)
db.close()