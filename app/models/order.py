import sqlite3
from app.utils.db_utils import get_db_path

class Order:
    def __init__(self, order_id=None, item_number=None, quantity=None, date_ordered=None):
        self.order_id = order_id
        self.item_number = item_number
        self.quantity = quantity
        self.date_ordered = date_ordered

    @classmethod
    def find_by_order_id(cls, order_id):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM orders WHERE order_id=?"
        cursor.execute(query, (order_id,))
        record = cursor.fetchone()

        if record:
            order = cls(*record)
        else:
            order = None

        conn.close()
        return order

    @classmethod
    def find_all(cls):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM orders"
        cursor.execute(query)
        records = cursor.fetchall()

        orders = [cls(*record) for record in records]

        conn.close()
        return orders

    def save_to_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        if self.order_id:  # Update existing order
            query = """UPDATE orders SET item_number=?, quantity=?, date_ordered=?
                       WHERE order_id=?"""
            cursor.execute(query, (self.item_number, self.quantity, self.date_ordered, self.order_id))
        else:  # Insert new order
            query = """INSERT INTO orders (item_number, quantity, date_ordered)
                       VALUES (?, ?, ?)"""
            cursor.execute(query, (self.item_number, self.quantity, self.date_ordered))
            self.order_id = cursor.lastrowid

        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "DELETE FROM orders WHERE order_id=?"
        cursor.execute(query, (self.order_id,))

        conn.commit()
        conn.close()
