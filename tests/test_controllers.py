import unittest
from app.controllers import authentication_controller, inventory_controller, order_controller, review_controller, supplier_controller

class TestControllers(unittest.TestCase):

    # Tests for authentication_controller
    def test_register_and_authenticate_user(self):
        success, message = authentication_controller.register_user("testuser", "testpassword", "testuser@example.com")
        self.assertTrue(success)

        success, message = authentication_controller.authenticate_user("testuser", "testpassword")
        self.assertTrue(success)

    # Tests for inventory_controller
    def test_inventory_operations(self):
        success = inventory_controller.add_item("TestItem", 100.0, "Test Description", "/path/to/image.jpg")
        self.assertTrue(success)

        items = inventory_controller.get_all_items()
        self.assertIsNotNone(items)

        item = inventory_controller.get_item_by_item_number(1)  # Assuming it's the first item
        self.assertIsNotNone(item)

    # Tests for order_controller
    def test_order_operations(self):
        # Assuming you have methods like add_order, get_all_orders, etc.
        success = order_controller.add_order(1, 5)  # item_number, quantity
        self.assertTrue(success)

        orders = order_controller.get_all_orders()
        self.assertIsNotNone(orders)

    # Tests for review_controller
    def test_review_operations(self):
        success = review_controller.add_review(1, "Test Review", 5)  # item_number, review_text, rating
        self.assertTrue(success)

        reviews = review_controller.get_all_reviews()
        self.assertIsNotNone(reviews)

    # Tests for supplier_controller
    def test_supplier_operations(self):
        success = supplier_controller.add_supplier("TestSupplier", "testsupplier@example.com")
        self.assertTrue(success)

        suppliers = supplier_controller.get_all_suppliers()
        self.assertIsNotNone(suppliers)

    # ... Add more tests ...

if __name__ == '__main__':
    unittest.main()
