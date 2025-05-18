# Import necessary modules
from decouple import config  # For loading environment variables securely
import mysql.connector       # MySQL database connector


def connect_db():
    """
    Establish a connection to the MySQL database.
    
    Returns:
        A MySQL connection object configured with credentials from the environment.
    """
    return mysql.connector.connect(
        host="localhost",      # Database server location
        user=config("DB_USER"),         # Database username from .env file
        password=config("DB_PASSWORD"), # Database password from .env file
        database="ALX_prodev"           # Target database name
    )


def stream_users():
    """
    Generator function that streams user records one at a time from the database.
    
    Yields:
        Dictionary-like row object representing a single user record.
    """
    connection = connect_db()                # Connect to the database
    cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for named access

    # Execute query to fetch all user data
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    # Yield each row individually for memory-efficient streaming
    for row in cursor:
        yield row

    # Clean up resources
    cursor.close()
    connection.close()
