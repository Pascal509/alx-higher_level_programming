#!/usr/bin/python3
import sys
import MySQLdb

MyConnect=MySQLdb.connect(host="localhost", port=3306, user="root", database="hbtn_0e_0_usa")

cursor = MyConnect.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

rows=cursor.fetchall()
for row in rows:
    print(row)

MyConnect.close()
