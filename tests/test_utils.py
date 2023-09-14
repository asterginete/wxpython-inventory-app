import unittest
import os
from app.utils import barcode_utils, image_utils, notification_utils, db_utils

class TestUtils(unittest.TestCase):

    # Tests for barcode_utils
    def test_generate_barcode(self):
        output_path = barcode_utils.generate_barcode("1234567890")
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)  # Cleanup

    def test_read_barcode_from_image(self):
        # Assuming you have a barcode image named 'test_barcode.png' with data "1234567890"
        data = barcode_utils.read_barcode_from_image('test_barcode.png')
        self.assertEqual(data, "1234567890")

    # Tests for image_utils
    def test_resize_image(self):
        # Assuming you have a test image named 'test_image.jpg'
        output_path = 'resized_test_image.jpg'
        image_utils.resize_image('test_image.jpg', output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)  # Cleanup

    # Tests for db_utils
    def test_get_db_path(self):
        path = db_utils.get_db_path()
        self.assertTrue(path.endswith('inventory_management.db'))

    # ... Add more tests ...

    # Note: For functions like sending emails or interacting with external services, 
    # you might want to use mock objects or skip testing them in unit tests.

if __name__ == '__main__':
    unittest.main()
