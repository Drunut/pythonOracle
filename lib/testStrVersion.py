#!/usr/bin/python

# Import necessary libraries.
import sys, cx_Oracle

# Add to the environment Python path.
# Appending run-time path with a new location
sys.path.append("/home/student/Code/python/lib")

# Import local library module.
from strOracle import formatVersion

# Create a connection.
db = cx_Oracle.connect("student/student@xe")

# Get the version of the database.
s = db.version

# Call the library funcxtion to format the version.
print formatVersion(s)