#!/usr/bin/python3

"""import modules"""
import sys
import MySQLdb


def main():
    """
    write a script that takes in arguments and displays all
    values in the states table of hbtn_0e_0_usa where name
    matchesthe argument. But this time, write one that is safe
    from MySQL injections!
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connect to mysql server"""
    MyConnect = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = MyConnect.cursor()

    """Execute Server"""
    cursor.execute("SELECT * FROM states WHERE name = %s "
                   "ORDER BY states.id ASC", (sys.argv[4],))

    """Iterate over each row and fetch data"""
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """Close server"""
    MyConnect.close()


if __name__ == "__main__":
    main()
