from app.models import Supplier

def get_all_suppliers():
    """
    Fetches all suppliers from the database.
    :return: List of Supplier objects.
    """
    return Supplier.find_all()

def get_supplier_by_id(supplier_id):
    """
    Fetches a supplier by its ID.
    :param supplier_id: ID of the supplier.
    :return: Supplier object or None if not found.
    """
    return Supplier.find_by_id(supplier_id)

def add_supplier(name, contact_info):
    """
    Adds a new supplier to the database.
    :param name: Name of the supplier.
    :param contact_info: Contact information of the supplier.
    :return: True if successful, False otherwise.
    """
    try:
        supplier = Supplier(name=name, contact_info=contact_info)
        supplier.save_to_db()
        return True
    except Exception as e:
        print(f"Error adding supplier: {e}")
        return False

def update_supplier(supplier_id, name, contact_info):
    """
    Updates an existing supplier in the database.
    :param supplier_id: ID of the supplier to be updated.
    :param name: Updated name.
    :param contact_info: Updated contact information.
    :return: True if successful, False otherwise.
    """
    supplier = Supplier.find_by_id(supplier_id)
    if not supplier:
        return False

    supplier.name = name
    supplier.contact_info = contact_info

    try:
        supplier.save_to_db()
        return True
    except Exception as e:
        print(f"Error updating supplier: {e}")
        return False

def delete_supplier(supplier_id):
    """
    Deletes a supplier from the database.
    :param supplier_id: ID of the supplier to be deleted.
    :return: True if successful, False otherwise.
    """
    supplier = Supplier.find_by_id(supplier_id)
    if not supplier:
        return False

    try:
        supplier.delete_from_db()
        return True
    except Exception as e:
        print(f"Error deleting supplier: {e}")
        return False
