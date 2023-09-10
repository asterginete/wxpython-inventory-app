from app.models import Item

def get_all_items():
    """
    Fetches all items from the inventory database.
    :return: List of Item objects.
    """
    return Item.find_all()

def get_item_by_item_number(item_number):
    """
    Fetches an item by its item number.
    :param item_number: Item number of the desired item.
    :return: Item object or None if not found.
    """
    return Item.find_by_item_number(item_number)

def add_item(item_name, price, description, image_link):
    """
    Adds a new item to the inventory database.
    :param item_name: Name of the item.
    :param price: Price of the item.
    :param description: Description of the item.
    :param image_link: Image link/path for the item.
    :return: True if successful, False otherwise.
    """
    try:
        item = Item(item_name=item_name, price=price, description=description, image_link=image_link)
        item.save_to_db()
        return True
    except Exception as e:
        print(f"Error adding item: {e}")
        return False

def update_item(item_number, item_name, price, description, image_link):
    """
    Updates an existing item in the inventory database.
    :param item_number: Item number of the item to be updated.
    :param item_name: Updated name of the item.
    :param price: Updated price of the item.
    :param description: Updated description of the item.
    :param image_link: Updated image link/path for the item.
    :return: True if successful, False otherwise.
    """
    item = Item.find_by_item_number(item_number)
    if not item:
        return False

    item.item_name = item_name
    item.price = price
    item.description = description
    item.image_link = image_link

    try:
        item.save_to_db()
        return True
    except Exception as e:
        print(f"Error updating item: {e}")
        return False

def delete_item(item_number):
    """
    Deletes an item from the inventory database.
    :param item_number: Item number of the item to be deleted.
    :return: True if successful, False otherwise.
    """
    item = Item.find_by_item_number(item_number)
    if not item:
        return False

    try:
        item.delete_from_db()
        return True
    except Exception as e:
        print(f"Error deleting item: {e}")
        return False
