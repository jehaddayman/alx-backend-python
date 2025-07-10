#!/usr/bin/python3
from seed import connect_to_prodev


def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that lazily loads pages of users from the database.
    """
    offset = 0
    while True:
        users = paginate_users(page_size, offset)
        if not users:
            break
        yield users
        offset += page_size
