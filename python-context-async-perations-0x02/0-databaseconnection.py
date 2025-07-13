#!/usr/bin/env python3
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        # فتح الاتصال بقاعدة البيانات
        self.connection = sqlite3.connect(self.db_name)
        return self.connection  # سيتم إسناد هذا المتغير إلى المتغير بعد كلمة "as"

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()  # إغلاق الاتصال بقاعدة البيانات

# الاستخدام الفعلي للـ context manager
if __name__ == "__main__":
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
