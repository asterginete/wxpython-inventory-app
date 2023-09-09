import sqlite3
from app.utils.db_utils import get_db_path

class User:
    def __init__(self, user_id=None, username=None, password=None):
        self.user_id = user_id
        self.username = username
        self.password = password  # Note: In a real-world scenario, you'd never store plain-text passwords.

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username=?"
        cursor.execute(query, (username,))
        record = cursor.fetchone()

        if record:
            user = cls(*record)
        else:
            user = None

        conn.close()
        return user

    @classmethod
    def find_by_id(cls, user_id):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE user_id=?"
        cursor.execute(query, (user_id,))
        record = cursor.fetchone()

        if record:
            user = cls(*record)
        else:
            user = None

        conn.close()
        return user

    def save_to_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        if self.user_id:  # Update existing user
            query = "UPDATE users SET username=?, password=? WHERE user_id=?"
            cursor.execute(query, (self.username, self.password, self.user_id))
        else:  # Insert new user
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            cursor.execute(query, (self.username, self.password))
            self.user_id = cursor.lastrowid

        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "DELETE FROM users WHERE user_id=?"
        cursor.execute(query, (self.user_id,))

        conn.commit()
        conn.close()
