import asyncio
import aiosqlite

# Asynchronous function to fetch all users from the database
async def async_fetch_users():
    database_name = "ALX_prodev"
    async with aiosqlite.connect(database_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
            print("All users:")
            for row in results:
                print(row)
    return

# Asynchronous function to fetch users older than 40 years
async def async_fetch_older_users():
    database_name = "ALX_prodev"
    async with aiosqlite.connect(database_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            results = await cursor.fetchall()
            print("Users older than 40:")
            for row in results:
                print(row)
    return

# Main function to set up the database and perform concurrent fetching
async def fetch_concurrently():
    database_name = "ALX_prodev"

    # Create the table and insert sample data
    async with aiosqlite.connect(database_name) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL
            )
        """)
        # Insert sample users into the table
        await db.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("John Doe", 30, "john.doe@example.com"))
        await db.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Jane Doe", 50, "jane.doe@example.com"))
        await db.commit()

    # Run both fetch operations concurrently
    await asyncio.gather(
        async_fetch_users(), 
        async_fetch_older_users()
    )

# Entry point for running the asynchronous tasks
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
