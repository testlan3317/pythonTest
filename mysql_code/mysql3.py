import mysql.connector

# creating a connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "testuser",
    password = "test@123"
)

#db.cursor()
mycursor = mydb.cursor()

#cursor.execute()
mycursor.execute("show databases")

for x in mycursor:
    print(x)  # output tuple
