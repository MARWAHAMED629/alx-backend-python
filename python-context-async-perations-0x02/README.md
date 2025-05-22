# Python Context Managers and Asynchronous Programming

## 🚀 Project Overview
This project focuses on mastering **context managers** and **asynchronous programming** in Python. You will build custom class-based context managers for database operations and explore running database queries concurrently using the `aiosqlite` library.

> **Level**: Novice  
> **Weight**: 1  
> **Start Date**: May 18, 2025 – **Deadline**: May 25, 2025  
> ✅ **Manual QA review required**  
> 🧪 Auto review will be launched at the deadline

---

## 🧠 Learning Objectives

By completing this project, you will:

- Understand and implement class-based context managers using `__enter__` and `__exit__` methods.
- Manage SQLite database connections cleanly and safely using context managers.
- Write reusable and parameterized database query handlers.
- Execute concurrent database queries asynchronously using `asyncio` and `aiosqlite`.
- Gain hands-on experience with real-world async patterns in Python.

---

## 🗂️ Project Structure

**Repository**: `alx-backend-python`  
**Directory**: `python-context-async-perations-0x02`


---

## ✅ Tasks & Descriptions

### `0. Custom Class-Based Context Manager for Database Connection`
- **File**: `0-databaseconnection.py`
- **Goal**: Create a class `DatabaseConnection` to handle connecting and closing a SQLite database.
- **Functionality**:
  - Implements `__enter__` and `__exit__` methods.
  - Fetches all users using `SELECT * FROM users`.

---

### `1. Reusable Query Context Manager`
- **File**: `1-execute.py`
- **Goal**: Create a reusable context manager `ExecuteQuery` that executes any given SQL query with optional parameters.
- **Functionality**:
  - Handles both connection and query execution.
  - Example: `SELECT * FROM users WHERE age > ?` with parameter `25`.

---

### `2. Concurrent Asynchronous Database Queries`
- **File**: `3-concurrent.py`
- **Goal**: Use `asyncio` and `aiosqlite` to perform concurrent database queries.
- **Functionality**:
  - `async_fetch_users()` fetches all users.
  - `async_fetch_older_users()` fetches users older than 40.
  - Uses `asyncio.gather()` to run them in parallel.

---

## 🧰 Requirements

- Python 3.8 or higher
- `aiosqlite` installed (`pip install aiosqlite`)
- SQLite database file (`ALX_prodev`) with a `users` table for testing
- Basic knowledge of context managers and async programming in Python

---
