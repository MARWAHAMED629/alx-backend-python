from decouple import config
from mysql.connector import Error, connect
import csv
import uuid
import os


# Function to establish a connection to the MySQL server
def connect_db():
    """Connect to the MySQL database server."""
    try:
        connection = connect(
            host="localhost",
            user=config("DB_USER"),
            password=config("DB_PASSWORD")
        )
        if connection.is_connected():
            print("Successfully connected to the database server.")
        return connection
    except Error as e:
        print(f"Failed to connect to MySQL server: {e}")
        return None


# Create ALX_prodev database if it doesn't exist
def create_database(connection):
    """Create the database 'ALX_prodev' if it does not already exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()


# Connect directly to the ALX_prodev database
def connect_to_prodev():
    """Establish a connection specifically to the ALX_prodev database."""
    connection = connect_db()
    connection.database = "ALX_prodev"
    return connection


# Create the 'user_data' table if it does not exist
def create_table(connection):
    """Create the 'user_data' table with UUID-based primary key and basic fields."""
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(10, 2) NOT NULL
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()


# Insert data into the 'user_data' table
def insert_data(connection, data):
    """Insert processed data into the 'user_data' table."""
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO user_data (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    """
    for row in data:
        cursor.execute(insert_query, row)
    connection.commit()
    cursor.close()


# Load and process CSV file into structured data with UUIDs
def load_data_from_csv(file_name="user_data.csv"):
    """Load and parse data from a CSV file, skipping malformed or incomplete rows."""
    data = []
    file_path = os.path.join(os.getcwd(), file_name)

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header

            for row in csvreader:
                if len(row) < 3:
                    print(f"Skipping incomplete row: {row}")
                    continue

                name, email, age_str = map(str.strip, row[:3])

                if not all([name, email, age_str]):
                    print(f"Skipping row with missing values: {row}")
                    continue

                try:
                    age = float(age_str)
                except ValueError:
                    print(f"Invalid age format in row: {row}")
                    continue

                user_id = str(uuid.uuid4())
                data.append((user_id, name, email, age))

        print(f"Successfully loaded {len(data)} valid records from '{file_name}'.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Unexpected error while loading CSV: {e}")

    return data


# Generator function to stream data from the database row by row
def stream_rows_from_db():
    """Stream rows from the 'user_data' table one at a time using a generator."""
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor.close()
    connection.close()


# Main function to orchestrate database setup and data insertion
def main():
    """Main function to set up database, table, and populate data from CSV."""
    try:
        # Step 1: Connect to MySQL and create database if needed
        connection = connect_db()
        create_database(connection)
        connection.close()

        # Step 2: Reconnect to ALX_prodev database and create table
        connection = connect_to_prodev()
        create_table(connection)

        # Step 3: Load data from CSV and insert into database
        file_path = "user_data.csv"
        data = load_data_from_csv(file_path)
        if data:
            insert_data(connection, data)
        else:
            print("No valid data to insert.")
        
        connection.close()

        # Step 4: Stream and display stored data
        print("Streaming data from the database:")
        for row in stream_rows_from_db():
            print(row)

    except Error as err:
        print(f"MySQL error occurred: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    main()
