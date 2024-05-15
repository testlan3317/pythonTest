import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "testuser",
    password = "test@123",
    database = "DBTEST"
    )

mycursor = mydb.cursor()


# alter table customer add column id int auto_increment primary key
# DROP TABLE IF EXISTS device

mycursor.execute("""delete from device""")
mycursor.execute("""drop table device if exists device""")
mycursor.execute(""" 
    create table device (
        oid int(11) not null auto_increment primary key,
        sn char(16) unique not null,
        region varchar(255) not null,
        timezone double not null,
        dc int(11),
        server1 int(11),
        server2 int(11),
        update_time int(10) unsigned default 0,
        create_time int(10) unsigned default 0
    )"""
    )


# insert a record into the table
sql = "insert into device (sn, region, timezone, dc, server1, server2, update_time, create_time) values (%s, %s, %s, %s, %s, %s, %s, %s)"
create_time = int(datetime.datetime.now().timestamp())

val = ("FGVM04TM22090163", "burnaby", -8, 1, 26, 27, 0, create_time)
mycursor.execute(sql, val)    # cursor.execute()  single
# mycursor will only remeber the last execute return
vals = [
("FGVM04TMXXXXX", "burnaby", -8, 1, 23, 24, 0, create_time),
("FGVM04TMXXXXX", "burnaby", -8, 1, 28, 29, 0, create_time),
("FGVM04TMXXXXX", "burnaby", -8, 1, 21, 22, 0, create_time),
        ]

mycursor.executemany(sql, vals)   # cursor.executemany()  for multiple records

# connection.commit() the transaction
# action relate: INSERT, UPDATE, DELETE
mydb.commit()

print(mycursor.rowcount, "record inserted.")   # cursor.rowcount --> get inserted record for the last cursor work
print("last row id", mycursor.lastrowid)

mydb.close()

'''
You must use %d for integer values and %s for string values.

You can also use %f for floating point value, %b for binary data and %% Just to insert a percent symbol.
'''