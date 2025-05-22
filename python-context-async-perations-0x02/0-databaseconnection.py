import sqlite3

# Define a context manager class for handling database connections
class DatabaseConnection():
    def __init__(self, ALX_prodev):
        # Store the database name
        self.database_name = ALX_prodev
        self.connection = None

    def __enter__(self):
        # Establish a connection and return the cursor
        self.connection = sqlite3.connect(self.database_name)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit if no exceptions occurred, then close the connection
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            self.connection.close()

# Execute only if the script is run directly
if __name__ == "__main__":
    database_name = "ALX_prodev"

    # Create 'users' table if it does not exist
    with DatabaseConnection(database_name) as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

    # Select and print all users from the 'users' table
    with DatabaseConnection(database_name) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
