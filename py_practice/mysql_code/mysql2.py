import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "testuser",
    password = "test@123"
)


mycursor = mydb.cursor()


mycursor.execute("CREATE DATABASE DBTEST")

