import sqlite3
import functools

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        print(f"Executing SQL query: {query}")
        return func(*args, **kwargs)
    return wrapper
