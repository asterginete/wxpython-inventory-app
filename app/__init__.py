from .utils import init_db

# Initialize the database
init_db()

# Import necessary modules for the application
from . import models
from . import controllers
from . import views
from . import utils
