#!/usr/bin/python3
"""
Takes name of a state as arguement and lists it
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

        # Create the SQL query to fetch cities of the specified state
        query = "SELECT cities.name " \
                "FROM cities " \
                "INNER JOIN states ON cities.state_id = states.id " \
                "WHERE states.name = %s " \
                "ORDER BY cities.id ASC"

        # Execute the SQL query with parameter substitution to prevent SQL injection
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        cities = cursor.fetchall()

        # Extract city names from the result and join them into a single string
        city_names = ', '.join(city[0] for city in cities)

        # Print the results
        print(city_names)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
