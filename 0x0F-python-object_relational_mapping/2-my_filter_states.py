#!/usr/bin/python3
import sys
import MySQLdb
"""
Write a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    SearchedState = sys.argv[4]

    MyConnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passswd=password,
            db=database,
            GetState=SearchedState)

    cursor = MyConnect.cursor()

#SELECT * FROM states ORDER BY id ASC
    cursor.execute("SELECT * FROM states FORMAT(GetState)")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    MyConnect.close()


if __name__== "__main__":
    main()
