import sqlite3

DATABASE_PATH = "db/ecommerce_inventory.db"

def connect_to_db():
    """
    Connect to the SQLite database and return the connection.
    """
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def initialize_db():
    """
    Initialize the database by creating the necessary tables.
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        item_number INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image_link TEXT,
        date_of_registration DATE DEFAULT CURRENT_DATE
    )
    """)
    
    connection.commit()
    connection.close()

def insert_item(item):
    """
    Insert a new item into the database.
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO items (item_name, price, description, image_link) VALUES (?, ?, ?, ?)", 
                   (item.item_name, item.price, item.description, item.image_link))
    
    connection.commit()
    connection.close()

def fetch_all_items():
    """
    Fetch all items from the database.
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    
    cursor.execute("SELECT item_number, item_name, price, description, image_link FROM items")
    rows = cursor.fetchall()
    
    connection.close()
    
    return [Item.from_db_row(row) for row in rows]

def search_items(query):
    """
    Search items based on a query string.
    """
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # Using a LIKE query for a simple search. This can be enhanced further.
    cursor.execute("SELECT item_number, item_name, price, description, image_link FROM items WHERE item_name LIKE ?", 
                   ('%' + query + '%',))
    rows = cursor.fetchall()
    
    connection.close()
    
    return [Item.from_db_row(row) for row in rows]
