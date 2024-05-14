# to communicate with mysql should have mysql driver installed
# pip install mysql-connector-python


import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "testuser",
    password = "test@123"
)

print(mydb)
