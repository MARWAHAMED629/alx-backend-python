# Import required modules
import mysql.connector       # For connecting to MySQL database
from decouple import config  # For loading sensitive configuration from .env file


def connect_to_prodev():
    """
    Establish a connection to the 'ALX_prodev' MySQL database.

    Returns:
        A MySQL connection object using credentials from environment variables.
    """
    return mysql.connector.connect(
        host="localhost",           # The database server location
        user=config("DB_USER"),     # Database username (loaded securely from .env)
        password=config("DB_PASSWORD"),  # Database password (loaded securely from .env)
        database="ALX_prodev"       # Target database name
    )


def paginate_users(page_size, offset):
    """
    Fetch a specific page of users from the database using LIMIT and OFFSET.

    Args:
        page_size (int): Number of records to retrieve per page.
        offset (int): Starting point in the dataset for this page.

    Returns:
        List of dictionary-like rows representing users on the requested page.
    """
    connection = connect_to_prodev()                 # Connect to the database
    cursor = connection.cursor(dictionary=True)      # Use dictionary cursor for easier access

    # Execute SQL query with pagination using LIMIT and OFFSET
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")

    rows = cursor.fetchall()  # Retrieve all rows from the current page
    connection.close()        # Close the connection after fetching data
    return rows               # Return the fetched page of data


def lazy_paginate(page_size):
    """
    Generator function that yields pages of users one at a time.

    Args:
        page_size (int): Number of records to fetch per page.

    Yields:
        List of dictionary-like rows representing a single page of users.
    """
    offset = 0  # Start from the beginning of the dataset

    while True:
        # Fetch the current page of users
        page = paginate_users(page_size, offset)

        if not page:  # If no more data is returned, stop the loop
            break

        yield page    # Yield the current page for processing
        offset += page_size  # Move to the next batch by increasing the offset
