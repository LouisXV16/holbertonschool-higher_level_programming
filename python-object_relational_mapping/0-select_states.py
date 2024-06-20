#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        # Get MySQL credentials and database name from command line arguments
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Connect to MySQL server on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306
        )

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute SQL query to select all states, sorted by id in ascending order
        cur.execute("SELECT id, name FROM states ORDER BY id ASC")

        # Fetch all the results from the executed query
        rows = cur.fetchall()

        # Loop through the results and print each row
        for row in rows:
            print(row)

        # Close the cursor and the database connection
        cur.close()
        db.close()

    except IndexError:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)
    except MySQLdb.OperationalError as e:
        print(f"Error: {e}")
        sys.exit(1)
