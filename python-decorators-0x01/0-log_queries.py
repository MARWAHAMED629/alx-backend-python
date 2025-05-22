import sqlite3
import functools
from datetime import datetime

# Decorator that logs SQL queries with timestamps before executing them
def log_queries(func):
    @functools.wraps(func)
    def wrapper(query, *args, **kwargs):
        query = args[0] if args else kwargs.get('query', 'No Query')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Executing SQL query: {query}")  
        return func(*args, **kwargs)     
    return wrapper

# Function to fetch all users from the database, decorated to log the query
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Call the function to retrieve all users from the users table
users = fetch_all_users(query="SELECT * FROM users")
