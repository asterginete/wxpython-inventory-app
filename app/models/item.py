import sqlite3
from app.utils.db_utils import get_db_path

class Item:
    def __init__(self, item_number=None, item_name=None, price=None, description=None, image_link=None, date_of_registration=None):
        self.item_number = item_number
        self.item_name = item_name
        self.price = price
        self.description = description
        self.image_link = image_link
        self.date_of_registration = date_of_registration

    @classmethod
    def find_by_item_number(cls, item_number):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM items WHERE item_number=?"
        cursor.execute(query, (item_number,))
        record = cursor.fetchone()

        if record:
            item = cls(*record)
        else:
            item = None

        conn.close()
        return item

    @classmethod
    def find_all(cls):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM items"
        cursor.execute(query)
        records = cursor.fetchall()

        items = [cls(*record) for record in records]

        conn.close()
        return items

    def save_to_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        if self.item_number:  # Update existing item
            query = """UPDATE items SET item_name=?, price=?, description=?, image_link=?, date_of_registration=?
                       WHERE item_number=?"""
            cursor.execute(query, (self.item_name, self.price, self.description, self.image_link, self.date_of_registration, self.item_number))
        else:  # Insert new item
            query = """INSERT INTO items (item_name, price, description, image_link, date_of_registration)
                       VALUES (?, ?, ?, ?, ?)"""
            cursor.execute(query, (self.item_name, self.price, self.description, self.image_link, self.date_of_registration))
            self.item_number = cursor.lastrowid

        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "DELETE FROM items WHERE item_number=?"
        cursor.execute(query, (self.item_number,))

        conn.commit()
        conn.close()
