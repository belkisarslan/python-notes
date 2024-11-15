import sqlite3

connection = sqlite3.connect("person.db")
cursor = connection.cursor()

##birinci adım
##cursor.execute("CREATE TABLE persons(first_name TEXT, last_name TEXT, age INTEGER)")

##ikinci adım
##cursor.execute("INSERT INTO persons VALUES('person1','person2',21)")

cursor.execute("SELECT * FROM persons")
print(cursor.fetchall())

connection.commit()
connection.cursor()