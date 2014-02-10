import MySQLdb

#Open connection
db = MySQLdb.connect("localhost","root","1234", "TESTDB")

#prepare cursor
cursor = db.cursor()

#prepare SQL query to INSERT
sql = """INSERT INTO employee( first_name,
	 last_name, age, sex, income)
	 VALUES ('Jhon', 'Smith', 20,'M', 2000)"""

try:
	#Execute sql
	cursor.execute(sql)
	#commint the changes
	db.commit()
except:
	#Rollback in case error
	db.rollback()

#disconnect from server
db.close()

