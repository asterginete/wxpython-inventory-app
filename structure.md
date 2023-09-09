wxpython-inventory-app
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   ├── registration_view.py
│   │   ├── items_view.py
│   │   ├── analytics_view.py
│   │   ├── order_view.py
│   │   ├── supplier_view.py
│   │   └── review_view.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   ├── category.py
│   │   ├── supplier.py
│   │   ├── order.py
│   │   └── review.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── authentication_controller.py
│   │   ├── inventory_controller.py
│   │   ├── order_controller.py
│   │   ├── supplier_controller.py
│   │   └── review_controller.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── db_utils.py
│   │   ├── notification_utils.py
│   │   ├── image_utils.py
│   │   └── barcode_utils.py
│   │
│   └── static/
│       ├── images/
│       └── icons/
│
├── db/
│   ├── ecommerce_inventory.db
│   └── migrations/
│
├── mobile_app/  (if you decide to implement the mobile version)
│   ├── main.py
│   └── ... (other Kivy related files and directories)
│
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_controllers.py
│   └── test_utils.py
│
├── Pipfile
└── Pipfile.lock
