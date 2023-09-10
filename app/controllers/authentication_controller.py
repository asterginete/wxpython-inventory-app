from app.models import User
import bcrypt

def register_user(username, password, email):
    """
    Registers a new user in the database.
    :param username: Username of the user.
    :param password: Password of the user.
    :param email: Email of the user.
    :return: True if successful, False otherwise.
    """
    # Check if the user already exists
    user = User.find_by_username(username)
    if user:
        return False, "Username already exists."

    # Hash the password for security
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        user = User(username=username, password=hashed_password, email=email)
        user.save_to_db()
        return True, "User registered successfully."
    except Exception as e:
        print(f"Error registering user: {e}")
        return False, "Error registering user."

def authenticate_user(username, password):
    """
    Authenticates a user based on the provided username and password.
    :param username: Username of the user.
    :param password: Password of the user.
    :return: True if authentication is successful, False otherwise.
    """
    user = User.find_by_username(username)
    if not user:
        return False, "User not found."

    # Check if the hashed password matches the one in the database
    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return True, "Authentication successful."
    else:
        return False, "Invalid password."

def change_password(username, old_password, new_password):
    """
    Changes the password for a user.
    :param username: Username of the user.
    :param old_password: Current password of the user.
    :param new_password: New password for the user.
    :return: True if change is successful, False otherwise.
    """
    user = User.find_by_username(username)
    if not user:
        return False, "User not found."

    # Check if the old password is correct
    if not bcrypt.checkpw(old_password.encode('utf-8'), user.password.encode('utf-8')):
        return False, "Incorrect old password."

    # Hash the new password and update in the database
    hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    user.password = hashed_new_password

    try:
        user.save_to_db()
        return True, "Password updated successfully."
    except Exception as e:
        print(f"Error updating password: {e}")
        return False, "Error updating password."
