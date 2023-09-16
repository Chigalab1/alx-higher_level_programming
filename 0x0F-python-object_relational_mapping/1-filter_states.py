import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all three command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    # Get MySQL credentials from command-line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to execute SQL queries
        cursor = db.cursor()

        # Define the SQL query to select states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

        # Execute the query
        cursor.execute(query)

        # Fetch all the rows and display the results
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

