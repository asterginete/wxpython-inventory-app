import sqlite3
from app.utils.db_utils import get_db_path

class Supplier:
    def __init__(self, supplier_id=None, name=None, contact_info=None):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_info = contact_info

    @classmethod
    def find_by_name(cls, name):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM suppliers WHERE name=?"
        cursor.execute(query, (name,))
        record = cursor.fetchone()

        if record:
            supplier = cls(*record)
        else:
            supplier = None

        conn.close()
        return supplier

    @classmethod
    def find_by_id(cls, supplier_id):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM suppliers WHERE supplier_id=?"
        cursor.execute(query, (supplier_id,))
        record = cursor.fetchone()

        if record:
            supplier = cls(*record)
        else:
            supplier = None

        conn.close()
        return supplier

    @classmethod
    def find_all(cls):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM suppliers"
        cursor.execute(query)
        records = cursor.fetchall()

        suppliers = [cls(*record) for record in records]

        conn.close()
        return suppliers

    def save_to_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        if self.supplier_id:  # Update existing supplier
            query = "UPDATE suppliers SET name=?, contact_info=? WHERE supplier_id=?"
            cursor.execute(query, (self.name, self.contact_info, self.supplier_id))
        else:  # Insert new supplier
            query = "INSERT INTO suppliers (name, contact_info) VALUES (?, ?)"
            cursor.execute(query, (self.name, self.contact_info))
            self.supplier_id = cursor.lastrowid

        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "DELETE FROM suppliers WHERE supplier_id=?"
        cursor.execute(query, (self.supplier_id,))

        conn.commit()
        conn.close()
