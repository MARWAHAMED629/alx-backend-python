# 0x03. Unittests and Integration Tests

## Description

This project focuses on the principles and implementation of **unit testing** and **integration testing** in Python. You will write tests using the `unittest` framework, leverage `mock` for isolating code, and apply `parameterized` for running test cases with multiple inputs.

The tests are based on real Python modules (`utils.py`, `client.py`, `fixtures.py`) and will ensure correctness, modularity, and resilience of your codebase.

---

## Learning Objectives

At the end of this project, you will be able to explain:

- The difference between **unit tests** and **integration tests**
- How to use **mocking** to isolate functions and simulate external dependencies
- How to **parameterize** tests to reduce repetition
- How to test functions, classes, properties, and HTTP requests without making real network calls

---

## Technologies

- Python 3.7
- Ubuntu 18.04 LTS
- `unittest`, `unittest.mock`, `parameterized`
- `pycodestyle` (v2.5)

---

## Requirements

- All Python files are executable and follow PEP8 (`pycodestyle`) style guide
- All modules, classes, and functions include proper docstrings
- All code is fully type-annotated
- No actual HTTP or database calls in unit tests (use mocks)
- A `README.md` file is mandatory (this file)

---

## Running Tests

To execute any test file, use the following command:

```bash
$ python3 -m unittest path/to/test_file.py
