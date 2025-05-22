import sqlite3

# Context manager class to execute SQL queries using 'with' statement
class ExecuteQuery:
    def __init__(self, ALX_prodev, query, params=None):
        # Initialize with database name, SQL query, and optional parameters
        self.database_name = ALX_prodev
        self.query = query
        self.params = params or ()
        self.connection = None

    def __enter__(self):
        # Open database connection and execute the query
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit changes if no exception occurred, then close the connection
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            self.connection.close()

# Run only if this file is executed directly
if __name__ == "__main__":
    database_name = "ALX_prodev"

    # Create 'users' table if it doesn't exist
    with ExecuteQuery(database_name, """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    """) as cursor:
        pass  # Table creation executed

    # Fetch and display users older than 25
    with ExecuteQuery(database_name, "SELECT * FROM users WHERE age > ?", (25,)) as cursor:
        results = cursor.fetchall()
        for row in results:
            print(row)
