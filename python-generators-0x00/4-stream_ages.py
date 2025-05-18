# Import necessary modules
import mysql.connector       # For connecting to MySQL database
from decouple import config  # For securely loading environment variables


def connect_to_prodev():
    """
    Establish a connection to the 'ALX_prodev' MySQL database.

    Returns:
        A MySQL connection object using credentials from environment variables.
    """
    return mysql.connector.connect(
        host="localhost",           # Database server location
        user=config("DB_USER"),     # Database username (from .env file)
        password=config("DB_PASSWORD"),  # Database password (from .env file)
        database="ALX_prodev"       # Target database name
    )


def stream_user_ages():
    """
    Generator function that streams user ages one at a time from the database.

    Yields:
        int: The age of a single user.
    """
    connection = connect_to_prodev()                 # Connect to the database
    cursor = connection.cursor(dictionary=True)      # Use dictionary cursor for easier access

    cursor.execute("SELECT age FROM user_data")      # Fetch only the 'age' column

    # Yield each age individually
    for row in cursor:
        yield row['age']  # Extract and yield just the age value

    connection.close()  # Close the database connection when done


def calculate_average_age():
    """
    Calculate the average age of all users by processing streamed data.

    Returns:
        float: The average age of users, or 0 if there are no users.
    """
    total_age = 0
    count = 0

    # Stream ages one by one and accumulate the total
    for age in stream_user_ages():
        total_age += age
        count += 1

    # Avoid division by zero if the table is empty
    if count == 0:
        return 0

    return total_age / count  # Return the calculated average


# Main logic: Calculate and display the average age
average_age = calculate_average_age()
print(f"Average age of users: {average_age}")
