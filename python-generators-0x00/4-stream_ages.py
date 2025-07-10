#!/usr/bin/python3
from seed import connect_to_prodev


def stream_user_ages():
    """
    Generator to yield user ages one by one.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age
    cursor.close()
    connection.close()


def average_age():
    """
    Calculates the average age using the generator without loading full dataset in memory.
    """
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    avg = total / count if count > 0 else 0
    print(f"Average age of users: {avg:.2f}")
