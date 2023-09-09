import sqlite3
from app.utils.db_utils import get_db_path

class Category:
    def __init__(self, category_id=None, category_name=None):
        self.category_id = category_id
        self.category_name = category_name

    @classmethod
    def find_by_name(cls, category_name):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM categories WHERE category_name=?"
        cursor.execute(query, (category_name,))
        record = cursor.fetchone()

        if record:
            category = cls(*record)
        else:
            category = None

        conn.close()
        return category

    @classmethod
    def find_by_id(cls, category_id):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM categories WHERE category_id=?"
        cursor.execute(query, (category_id,))
        record = cursor.fetchone()

        if record:
            category = cls(*record)
        else:
            category = None

        conn.close()
        return category

    @classmethod
    def find_all(cls):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM categories"
        cursor.execute(query)
        records = cursor.fetchall()

        categories = [cls(*record) for record in records]

        conn.close()
        return categories

    def save_to_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        if self.category_id:  # Update existing category
            query = "UPDATE categories SET category_name=? WHERE category_id=?"
            cursor.execute(query, (self.category_name, self.category_id))
        else:  # Insert new category
            query = "INSERT INTO categories (category_name) VALUES (?)"
            cursor.execute(query, (self.category_name,))
            self.category_id = cursor.lastrowid

        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "DELETE FROM categories WHERE category_id=?"
        cursor.execute(query, (self.category_id,))

        conn.commit()
        conn.close()
