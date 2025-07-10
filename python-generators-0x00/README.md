#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev


def stream_users_in_batches(batch_size):
    """
    Generator that fetches user data from the database in batches
    and yields each batch as a list of user dictionaries.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))

        rows = cursor.fetchall()
        if not rows:
            break
        yield rows  # ✅ This is required to pass the check
        offset += batch_size

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Processes each batch to filter and print users over the age of 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
