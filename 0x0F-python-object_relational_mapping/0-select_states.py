#!/usr/bin/python3
"""import MySQLdb module"""
import sys
import MySQLdb

"""
Write a script that lists all states from the
database hbtn_0e_0_usa

MyConnect connects to MySQL server
"""


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    MyConnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    """Create cursor object"""
    cursor = MyConnect.cursor()

    """Execute dbquery to fetch the states by their id"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch and print results row by row"""
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    """Close database connection"""
    MyConnect.close()


if __name__ == "__main__":
    main()
