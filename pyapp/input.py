import os
import sys
import getopt
import mysql.connector

def create_database_table():
    # Function to create the 'input' table in the database
    try:
        # Connect to the MySQL database (replace the placeholder values with your actual database credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crawler"
        )
        cursor = connection.cursor()

        # SQL statement to create the 'input' table if it doesn't exist
        create_table_query = """
            CREATE TABLE IF NOT EXISTS input (
                id INT AUTO_INCREMENT PRIMARY KEY,
                seed_url VARCHAR(255) NOT NULL,
                search_query VARCHAR(255) NOT NULL
            )
        """

        # Execute the SQL statement to create the table
        cursor.execute(create_table_query)

        # Commit the changes to the database and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error creating 'input' table in database - {e}")
        sys.exit(1)


def check_seed_url_exists(seed_url):
    # Function to check if the seed URL already exists in the 'input' table in the database
    try:
        # Connect to the MySQL database (replace the placeholder values with your actual database credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crawler"
        )
        cursor = connection.cursor()

        # Query the database to check if the seed URL exists in the 'input' table
        query = "SELECT seed_url FROM input WHERE seed_url = %s"
        cursor.execute(query, (seed_url,))

        # Fetch the result
        result = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # If the result is not None, it means the seed URL exists in the database
        return result is not None

    except mysql.connector.Error as e:
        print(f"Error checking seed URL in database - {e}")
        sys.exit(1)


def insert_seed_url(seed_url, search_query):
    # Function to insert the seed URL and search query into the 'input' table in the database
    try:
        # Connect to the MySQL database (replace the placeholder values with your actual database credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crawler"
        )
        cursor = connection.cursor()

        # SQL statement to insert the seed URL and search query into the table
        insert_query = "INSERT INTO input (seed_url, search_query) VALUES (%s, %s)"
        values = (seed_url, search_query)
        cursor.execute(insert_query, values)

        # Commit the changes to the database and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error inserting seed URL into database - {e}")
        sys.exit(1)


def main(argv):
    # Initialize variables to store user input
    seed_url = ""
    search_query = ""

    try:
        # Use getopt to parse command-line arguments and options
        opts, argv = getopt.getopt(argv, "u:q:", ["seed_url=", "search_query="])
    except getopt.GetoptError:
        # If there's an error in the command-line arguments, print usage instructions and exit
        print("input.py -u <seed_url> -q <search_query>")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u", "--seed_url"):
            # Store the value of the '-u' or '--seed_url' option as the seed URL
            seed_url = arg
        elif opt in ("-q", "--search_query"):
            # Store the value of the '-q' or '--search_query' option as the search query
            search_query = arg

    if not seed_url or not search_query:
        # If either the seed URL or search query is missing, print usage instructions and exit
        print("Please provide the seed URL and search query.")
        print("input.py -u <seed_url> -q <search_query>")
        sys.exit(2)

    # Create the 'input' table in the database if it doesn't exist
    create_database_table()

    # Check if the seed URL already exists in the database
    if check_seed_url_exists(seed_url):
        print("Seed URL already exists in the database. Skipping crawling process.")
        # Call search.py with the search query
        os.system(f"python pyapp/search.py {search_query}")  
    else:
        # Insert the seed URL and search query into the database
        insert_seed_url(seed_url, search_query)
        print(f"Inserted seed URL: {seed_url}")
        # os.system(f"python crawl.py {seed_url}")
        # Perform the crawling process here (not implemented in this script)
        print(f"Crawling seed URL: {seed_url}")
        # Call crawl.py with the seed URL
        os.system(f"python pyapp/crawl.py {seed_url}")
        os.system(f"python pyapp/search.py {search_query}") 

    # Now, you can pass the 'seed_url' and 'search_query' to the crawling and searching modules.
    # For now, we'll just print them to the console to demonstrate the input handling.
    # print(f"Search Query: {search_query}")

if __name__ == "__main__":
    # The script entry point. Call the 'main' function with command-line arguments (excluding the script name).
    main(sys.argv[1:])


