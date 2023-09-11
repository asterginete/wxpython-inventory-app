import sqlite3
import os

DB_NAME = "inventory_management.db"

def get_db_path():
    """
    Returns the path to the SQLite database.
    :return: Path to the SQLite database.
    """
    return os.path.join(os.getcwd(), DB_NAME)

def init_db():
    """
    Initializes the database by creating necessary tables.
    """
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    # Create tables
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    """

    create_items_table = """
    CREATE TABLE IF NOT EXISTS items (
        item_number INTEGER PRIMARY KEY,
        item_name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image_link TEXT,
        date_of_registration TEXT NOT NULL
    );
    """

    # ... Add other table creation statements as needed ...

    cursor.execute(create_users_table)
    cursor.execute(create_items_table)
    # ... Execute other table creation statements ...

    conn.commit()
    conn.close()

def execute_query(query, params=()):
    """
    Executes a query on the database.
    :param query: SQL query to be executed.
    :param params: Parameters for the SQL query.
    :return: Result of the query.
    """
    conn = sqlite3.connect(get_db_path())
    cursor = conn.cursor()

    cursor.execute(query, params)
    result = cursor.fetchall()

    conn.commit()
    conn.close()

    return result
