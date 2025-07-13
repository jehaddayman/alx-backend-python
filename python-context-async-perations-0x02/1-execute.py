#!/usr/bin/env python3
import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=()):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        # فتح الاتصال وتنفيذ الاستعلام
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_value, traceback):
        # تنظيف الموارد
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# استخدام الـ context manager
if __name__ == "__main__":
    db_name = "users.db"
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)

    with ExecuteQuery(db_name, query, params) as results:
        for row in results:
            print(row)
