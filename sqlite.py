import sqlite3

# Executing Multiple SQL Statements using executescript()

with sqlite3.connect("test_database.db") as connection:
	cursor = connection.cursor()
	cursor.executescript("""DROP TABLE IF EXISTS People;
	DROP TABLE IF EXISTS Peoples; 
	CREATE TABLE People(
	FirstName TEXT, 
	LastName TEXT, 
	Age INT); 
	INSERT INTO People VALUES(
	'Ron', 
	'Obvious', '66'
	);""")

# Working with DataBase Tables

with sqlite3.connect("test_database.db") as connection:
	cursor = connection.cursor()
	cursor.execute(""" CREATE TABLE Peoples(FirstName TEXT,Last_Name TEXT,Age INT);""")
	cursor.execute("""INSERT INTO Peoples VALUES('Ron','Obvious',25);""")




# Create a new table and insert values

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute(""" CREATE TABLE People(FirstName TEXT,Last_Name TEXT,Age INT);""")
cursor.execute("""INSERT INTO People VALUES('Ron','Obvious',25);""")
connection.commit()
connection.close()

# get data from a table

connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM People")
cursor.fetchone()






