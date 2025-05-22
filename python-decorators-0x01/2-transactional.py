import sqlite3
import functools

# Decorator that automatically opens and closes a database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to wrap a database operation inside a transaction
# Commits if successful, rolls back if an exception occurs
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  # Save changes
            return result
        except Exception as e:
            conn.rollback()  # Undo changes on error
            print(f"Transaction failed: {e}")  
            raise 
    return wrapper

# Function to update a user's email by user ID using a managed connection and transaction
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Attempt to update email and print result
try:
    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
    print("Email updated successfully.")
except Exception as e:
    print("Failed to update email:", e)
