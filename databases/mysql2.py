import MySQLdb

#open connection
db = MySQLdb.connect("localhost","root", "1234","TESTDB")

#prepare a cursor
cursor = db.cursor()

# Drop table if already exists
cursor.execute("DROP TABLE IF EXISTS employee")

#Create table as per requierement
sql = """CREATE TABLE employee (
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20),
	age INT,
	sex CHAR(1),
	income FLOAT)"""

cursor.execute(sql)

#disconnect from server
db.close()
