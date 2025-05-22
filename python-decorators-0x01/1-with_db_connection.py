import sqlite3
import functools

# Decorator to automatically handle database connection setup and teardown
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Function to retrieve a user record by ID using a managed database connection
@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch and print the user with ID = 1
user = get_user_by_id(user_id=1)
print(user)
