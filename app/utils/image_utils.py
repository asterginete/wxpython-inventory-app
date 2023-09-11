from PIL import Image
import os

def resize_image(input_path, output_path, base_width=300):
    """
    Resizes an image maintaining its aspect ratio.
    :param input_path: Path to the original image.
    :param output_path: Path to save the resized image.
    :param base_width: Desired width of the resized image. Height will be adjusted to maintain aspect ratio.
    """
    img = Image.open(input_path)
    w_percent = base_width / float(img.size[0])
    h_size = int(float(img.size[1]) * float(w_percent))
    img = img.resize((base_width, h_size), Image.ANTIALIAS)
    img.save(output_path)

def load_image(image_path):
    """
    Loads an image from a given path.
    :param image_path: Path to the image.
    :return: Image object.
    """
    return Image.open(image_path)

def save_image(image, output_path):
    """
    Saves an image to a specified path.
    :param image: Image object to be saved.
    :param output_path: Path to save the image.
    """
    image.save(output_path)

def delete_image(image_path):
    """
    Deletes an image from the specified path.
    :param image_path: Path to the image to be deleted.
    """
    if os.path.exists(image_path):
        os.remove(image_path)
