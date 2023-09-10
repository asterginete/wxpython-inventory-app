from app.models import Order

def get_all_orders():
    """
    Fetches all orders from the database.
    :return: List of Order objects.
    """
    return Order.find_all()

def get_order_by_id(order_id):
    """
    Fetches an order by its ID.
    :param order_id: ID of the order.
    :return: Order object or None if not found.
    """
    return Order.find_by_order_id(order_id)

def place_order(item_number, quantity):
    """
    Places a new order in the database.
    :param item_number: Item number associated with the order.
    :param quantity: Quantity of the item ordered.
    :return: True if successful, False otherwise.
    """
    try:
        order = Order(item_number=item_number, quantity=quantity)
        order.save_to_db()
        return True
    except Exception as e:
        print(f"Error placing order: {e}")
        return False

def update_order(order_id, item_number, quantity):
    """
    Updates an existing order in the database.
    :param order_id: ID of the order to be updated.
    :param item_number: Updated item number.
    :param quantity: Updated quantity.
    :return: True if successful, False otherwise.
    """
    order = Order.find_by_order_id(order_id)
    if not order:
        return False

    order.item_number = item_number
    order.quantity = quantity

    try:
        order.save_to_db()
        return True
    except Exception as e:
        print(f"Error updating order: {e}")
        return False

def delete_order(order_id):
    """
    Deletes an order from the database.
    :param order_id: ID of the order to be deleted.
    :return: True if successful, False otherwise.
    """
    order = Order.find_by_order_id(order_id)
    if not order:
        return False

    try:
        order.delete_from_db()
        return True
    except Exception as e:
        print(f"Error deleting order: {e}")
        return False
