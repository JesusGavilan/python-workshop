import MySQLdb

#Open database connection
db = MySQLdb.connect("localhost","root","1234","TESTDB")

#cursor object
cursor = db.cursor()

#execute SQL query
cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone() 
data = cursor.fetchone()

print "Database version : %s " % data

#disconnect from server
db.close()


