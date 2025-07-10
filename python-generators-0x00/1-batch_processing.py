#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """Generator that yields users in batches from the DB"""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()
        if not rows:
            break
        yield rows
        offset += batch_size

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """Processes batches, filters users over age 25, and prints them"""
    for batch in stream_users_in_batches(batch_size):  # loop 1
        for user in batch:  # loop 2
            if user["age"] > 25:
                print(user)  # still inside loop 2 (not a third loop)
