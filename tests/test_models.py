import unittest
from app.models import User, Item, Category, Supplier, Order, Review

class TestModels(unittest.TestCase):

    # Tests for User model
    def test_user_operations(self):
        user = User(username="testuser", password="hashedpassword", email="testuser@example.com")
        user.save_to_db()

        retrieved_user = User.find_by_username("testuser")
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, "testuser@example.com")

    # Tests for Item model
    def test_item_operations(self):
        item = Item(item_name="TestItem", price=100.0, description="Test Description", image_link="/path/to/image.jpg")
        item.save_to_db()

        retrieved_item = Item.find_by_item_name("TestItem")
        self.assertIsNotNone(retrieved_item)
        self.assertEqual(retrieved_item.price, 100.0)

    # Tests for Category model
    def test_category_operations(self):
        category = Category(name="TestCategory")
        category.save_to_db()

        retrieved_category = Category.find_by_name("TestCategory")
        self.assertIsNotNone(retrieved_category)

    # Tests for Supplier model
    def test_supplier_operations(self):
        supplier = Supplier(name="TestSupplier", email="testsupplier@example.com")
        supplier.save_to_db()

        retrieved_supplier = Supplier.find_by_name("TestSupplier")
        self.assertIsNotNone(retrieved_supplier)
        self.assertEqual(retrieved_supplier.email, "testsupplier@example.com")

    # Tests for Order model
    def test_order_operations(self):
        order = Order(item_number=1, quantity=5)  # Assuming item with item_number=1 exists
        order.save_to_db()

        retrieved_order = Order.find_by_id(order.order_id)
        self.assertIsNotNone(retrieved_order)
        self.assertEqual(retrieved_order.quantity, 5)

    # Tests for Review model
    def test_review_operations(self):
        review = Review(item_number=1, review_text="Test Review", rating=5)  # Assuming item with item_number=1 exists
        review.save_to_db()

        retrieved_review = Review.find_by_id(review.review_id)
        self.assertIsNotNone(retrieved_review)
        self.assertEqual(retrieved_review.rating, 5)

    # ... Add more tests ...

if __name__ == '__main__':
    unittest.main()
