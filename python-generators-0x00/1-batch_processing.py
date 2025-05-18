# Import required libraries
import mysql.connector       # For connecting to and interacting with MySQL databases
from decouple import config  # For securely loading environment variables from .env file


def connect_db():
    """
    Establish a connection to the MySQL database using credentials from environment variables.
    
    Returns:
        A MySQL connection object to the 'ALX_prodev' database.
    """
    return mysql.connector.connect(
        host="localhost",          # Host where the MySQL server is running
        user=config("DB_USER"),    # Database username loaded from environment variables
        password=config("DB_PASSWORD"),  # Database password loaded from environment variables
        database="ALX_prodev"      # Name of the target database
    )


def stream_users_in_batches(batch_size):
    """
    Generator function that streams data from the database in manageable batches.
    
    Args:
        batch_size (int): Number of records to fetch per batch.

    Yields:
        List of dictionary-like row objects representing a batch of users.
    """
    connection = connect_db()                 # Connect to the database
    cursor = connection.cursor(dictionary=True)  # Get rows as dictionaries for easier access

    # Execute SQL query to retrieve all user data
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    # Fetch and yield rows in batches to reduce memory usage
    while True:
        batch = cursor.fetchmany(batch_size)  # Retrieve a fixed number of rows
        if not batch:                         # Stop when there are no more rows
            break
        yield batch                           # Yield the current batch for processing

    # Clean up resources
    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Process each batch of users and filter those older than 25 years.
    
    Args:
        batch_size (int): Number of records to process at once.

    Yields:
        Dictionary containing details of users older than 25.
    """
    # Stream data in batches from the database
    for batch in stream_users_in_batches(batch_size):
        # Loop through each user in the current batch
        for user in batch:
            # Check if the user's age is greater than 25
            if user['age'] > 25:
                yield user  # Yield only the users who meet the condition
