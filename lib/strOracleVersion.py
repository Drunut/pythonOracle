#------------------------------------------------------------
#  Program name: strVersionOracle.py
#  Written by:   Michael McLaughlin
#  Dated:        2016-10-19
#  Purpose:      Define a library module for cx_Oracle
# ------------------------------------------------------------

# Parse and format Oracle version.
def formatVersion(s):

  # Split string into collection.
  list = s.split(".")
  #i is the iterator, l is the value of each list item
  for i, l in enumerate(list):
    if i == 0 and list[i] == "11":
      label = str(l) + "g"
    elif i == 0 and list[i] == "12":
      label = label + str(l) + "c"
    elif i == 1:
      label = label + "R" + list[i] + " (" + s + ")"

  # Rehowturn the augmented string.
  return label