# 🐍 Python Decorators for Database Operations

## 📘 Project Description

This project focuses on mastering **Python decorators** to enhance database operations in Python applications. Through hands-on tasks, developers will create custom decorators to:

- Log SQL queries  
- Handle database connections  
- Manage transactions  
- Retry failed operations  
- Cache query results  

The tasks simulate real-world challenges, providing an in-depth understanding of Python’s dynamic and reusable capabilities in database management.

---

## 🎯 Learning Objectives

By completing this project, developers will:

- ✅ Deepen their understanding of Python decorators and how to build reusable, clean code.
- ✅ Automate repetitive database tasks like connection handling, logging, and error management.
- ✅ Implement robust transaction handling with `commit` and `rollback` support.
- ✅ Introduce retry mechanisms for resilient database operations.
- ✅ Optimize performance by caching frequently run queries.
- ✅ Follow best practices in Python backend development.

---

## ⚙️ Requirements

Before you begin, make sure you have:

- Python 3.8 or higher  
- SQLite3 installed (default in Python distributions)  
- A test database `users.db` with a `users` table  
- Basic knowledge of decorators and SQL  
- Git and GitHub setup for version control  

---

## 🚀 Key Highlights & Tasks

### ✅ Task 0: Logging Database Queries
- Create a decorator that logs SQL queries with timestamps.
- Understand how to intercept function calls for debugging and monitoring.

### ✅ Task 1: Handle Database Connections
- Use a decorator to automatically manage `connect()` and `close()` operations.
- Eliminate redundant connection setup code.

### ✅ Task 2: Transaction Management
- Implement a decorator that manages transactions.
- Rollback on failure and commit on success to ensure data integrity.

### ✅ Task 3: Retry Failed Queries
- Build a decorator that retries failed database operations.
- Handle transient issues (e.g., temporary locks or connectivity issues).

### ✅ Task 4: Cache Database Queries
- Create a decorator that caches query results in memory.
- Improve performance by avoiding redundant DB access for identical queries.
