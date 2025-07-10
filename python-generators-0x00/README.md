# Python Generators – Task 0: Database Setup Script

This script sets up a MySQL database (`ALX_prodev`) and populates a `user_data` table using data from a CSV file (`user_data.csv`).

## 📌 Objectives

- Connect to a MySQL server
- Create a database `ALX_prodev` if it does not exist
- Create a table `user_data` with the following fields:
  - `user_id` (UUID, Primary Key, Indexed)
  - `name` (VARCHAR)
  - `email` (VARCHAR)
  - `age` (DECIMAL)
- Populate the table with sample data from `user_data.csv`

## 🧰 Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` package  
  Install with:  
  ```bash
  pip install mysql-connector-python
