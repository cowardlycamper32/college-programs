import sqlite3 as sl
from nlib import novasroutines as nr

cursor = nr.slConnectionManager('database.sqlite')
print("it worked")
data = ("Bob Marley", "Bob Marley", True)
nr.slAddRow(cursor, 'librarybooks', data)



