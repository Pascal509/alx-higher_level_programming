#!/usr/bin/python3
"""import module"""
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

    """Connects to mysql server"""
    MyConnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    """Cursor initiates execution"""
    cursor = MyConnect.cursor()

    """Executes mysql server"""
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))

    """Fetch database"""
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    """Close connection"""
    MyConnect.close()


if __name__ == "__main__":
    main()
