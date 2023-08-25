class Item:
    def __init__(self, item_number=None, item_name="", price=0.0, description="", image_link=""):
        self.item_number = item_number
        self.item_name = item_name
        self.price = price
        self.description = description
        self.image_link = image_link

    def __str__(self):
        return f"Item({self.item_number}, {self.item_name}, {self.price}, {self.description}, {self.image_link})"

    @classmethod
    def from_db_row(cls, row):
        """
        Create an Item instance from a database row tuple.
        """
        return cls(row[0], row[1], row[2], row[3], row[4])
