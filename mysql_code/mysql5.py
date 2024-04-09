import mysql.connector


try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "testuser",
        password = "test@123",
        database = "DBTEST"
    )

    #sql = "select sn, region, timezone, create_time, dc, server1, server2 from device"
    
    # Prevent SQL injection when use condition, use %s placeholder
    sn = ("FGVM04TM22090164",)
    sql1 = "select sn, region, timezone, create_time, update_time, dc, server1, server2 from device where sn=%s"
    mycursor = mydb.cursor()
   
    #mycursor.execute(sql)
    mycursor.execute(sql1, sn)

    # fetchall() method, which fetches all rows from the last executed statement.
    # fetchone() : fetch only one
    myresult = mycursor.fetchall()   
    print(type(myresult)) # get reuslt from mycursor to myresult (list type)
    for x in myresult:
        print(x)   # tuple
except:
    raise Exception("Error happens during db work")
finally:
    mydb.close()

# select * from customer limit 5 offset 2; # start from position 3 and retrieve 5 records.

"""
if choose to use single quote, don't forget "\"
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

"""
