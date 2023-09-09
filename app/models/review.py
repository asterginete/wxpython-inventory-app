import sqlite3
from app.utils.db_utils import get_db_path

class Review:
    def __init__(self, review_id=None, item_number=None, rating=None, comment=None, date_posted=None):
        self.review_id = review_id
        self.item_number = item_number
        self.rating = rating
        self.comment = comment
        self.date_posted = date_posted

    @classmethod
    def find_by_review_id(cls, review_id):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM reviews WHERE review_id=?"
        cursor.execute(query, (review_id,))
        record = cursor.fetchone()

        if record:
            review = cls(*record)
        else:
            review = None

        conn.close()
        return review

    @classmethod
    def find_all(cls):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "SELECT * FROM reviews"
        cursor.execute(query)
        records = cursor.fetchall()

        reviews = [cls(*record) for record in records]

        conn.close()
        return reviews

    def save_to_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        if self.review_id:  # Update existing review
            query = """UPDATE reviews SET item_number=?, rating=?, comment=?, date_posted=?
                       WHERE review_id=?"""
            cursor.execute(query, (self.item_number, self.rating, self.comment, self.date_posted, self.review_id))
        else:  # Insert new review
            query = """INSERT INTO reviews (item_number, rating, comment, date_posted)
                       VALUES (?, ?, ?, ?)"""
            cursor.execute(query, (self.item_number, self.rating, self.comment, self.date_posted))
            self.review_id = cursor.lastrowid

        conn.commit()
        conn.close()

    def delete_from_db(self):
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        query = "DELETE FROM reviews WHERE review_id=?"
        cursor.execute(query, (self.review_id,))

        conn.commit()
        conn.close()
