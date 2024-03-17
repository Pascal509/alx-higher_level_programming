#!/usr/bin/python3

"""Import modules"""
import sys
import MySQLdb

"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa

MyConnect conects to MySQL server
"""
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

Connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

"""Create cursor object"""
cursor = Connection.cursor()

""""
Execute query to fetch states starting with a name starting               with N
"""
cursor.execute("SELECT * FROM states WHERE UPPER(NAME) LIKE 'N%'")

"""Fetch states row by row"""
rows = cursor.fetchall()
for row in rows:
    print(row)

""""Close connection"""
cursor.close()
Connection.close()
