import mysql.connector # pip install mysql-connector-python

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb) 