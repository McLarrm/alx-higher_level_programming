#!/usr/bin/python3
"""
List all cities from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Create the SQL query to fetch cities with their corresponding states
        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities " \
                "INNER JOIN states ON cities.state_id = states.id " \
                "ORDER BY cities.id ASC"

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows
        cities = cursor.fetchall()

        # Print the results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
