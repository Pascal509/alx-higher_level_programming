#!/usr/bin/python3

import sys
import MySQLdb

def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connect to server"""
    MyConnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = MyConnect.cursor()

    """Execute Server"""
    cursor.execute("SELECT COUNT(sys.argv[4]) FROM {}".format(cities))
    """cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s")"""

    """Iterate over each row and fetch data"""
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """Close Server"""
    MyConnect.close()


if __name__ == "__main__":
    main()
