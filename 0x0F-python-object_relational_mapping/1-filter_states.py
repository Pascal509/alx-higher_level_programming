#!/usr/bin/python3

"""Import modules"""
import sys
import MySQLdb

"""
Write a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa

MyConnect conects to MySQL server
"""
Connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        database="hbtn_0e_0_usa")

"""Create cursor object"""
cursor = Connection.connect()

""""
Execute query to fetch states starting with a name starting               with N
"""
cursor.execute("SELECT * FROM states WHERE NAME LIKE 'N%'")

"""Fetch states row by row"""
rows = cursor.fetchall()
for row in rows:
    print(row)

""""Close connection"""
Connection.close()
