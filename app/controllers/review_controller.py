from app.models import Review

def get_all_reviews():
    """
    Fetches all reviews from the database.
    :return: List of Review objects.
    """
    return Review.find_all()

def get_review_by_id(review_id):
    """
    Fetches a review by its ID.
    :param review_id: ID of the review.
    :return: Review object or None if not found.
    """
    return Review.find_by_review_id(review_id)

def add_review(item_number, rating, comment):
    """
    Adds a new review to the database.
    :param item_number: Item number associated with the review.
    :param rating: Rating given in the review.
    :param comment: Comment provided in the review.
    :return: True if successful, False otherwise.
    """
    try:
        review = Review(item_number=item_number, rating=rating, comment=comment)
        review.save_to_db()
        return True
    except Exception as e:
        print(f"Error adding review: {e}")
        return False

def update_review(review_id, item_number, rating, comment):
    """
    Updates an existing review in the database.
    :param review_id: ID of the review to be updated.
    :param item_number: Updated item number.
    :param rating: Updated rating.
    :param comment: Updated comment.
    :return: True if successful, False otherwise.
    """
    review = Review.find_by_review_id(review_id)
    if not review:
        return False

    review.item_number = item_number
    review.rating = rating
    review.comment = comment

    try:
        review.save_to_db()
        return True
    except Exception as e:
        print(f"Error updating review: {e}")
        return False

def delete_review(review_id):
    """
    Deletes a review from the database.
    :param review_id: ID of the review to be deleted.
    :return: True if successful, False otherwise.
    """
    review = Review.find_by_review_id(review_id)
    if not review:
        return False

    try:
        review.delete_from_db()
        return True
    except Exception as e:
        print(f"Error deleting review: {e}")
        return False
