#!/usr/bin/python3

"""import module"""
import sys
import MySQLdb


def main():
    """
    Write a script that lists all cities from the database
    hbtn_0e_4_usa
    """
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "LEFT JOIN states ON state_id = states.id "
                   "ORDER BY cities.id ASC")

    """Iterate over each row and fetch data"""
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """Close Server"""
    MyConnect.close()


if __name__ == "__main__":
    main()
