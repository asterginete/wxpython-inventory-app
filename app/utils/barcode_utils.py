import barcode
from barcode.writer import ImageWriter
from PIL import Image
import cv2
from pyzbar.pyzbar import decode

def generate_barcode(data, barcode_type='code128', output_path='barcode.png'):
    """
    Generates a barcode image.
    :param data: Data to be encoded in the barcode.
    :param barcode_type: Type of barcode to generate. Default is 'code128'.
    :param output_path: Path to save the generated barcode image.
    :return: Path to the generated barcode image.
    """
    barcode_class = getattr(barcode, barcode_type.upper(), barcode.CODE128)
    barcode_instance = barcode_class(data, writer=ImageWriter(), add_checksum=True)
    filename = barcode_instance.save(output_path)
    return filename

def read_barcode_from_image(image_path):
    """
    Reads barcode data from an image.
    :param image_path: Path to the image containing the barcode.
    :return: Decoded data from the barcode or None if no barcode is found.
    """
    image = cv2.imread(image_path)
    barcodes = decode(image)

    if barcodes:
        return barcodes[0].data.decode('utf-8')
    return None

def read_barcode_from_camera(camera_index=0):
    """
    Reads barcode data using a camera.
    :param camera_index: Index of the camera to use. Default is the primary camera.
    :return: Decoded data from the barcode or None if no barcode is found.
    """
    cap = cv2.VideoCapture(camera_index)
    
    while True:
        ret, frame = cap.read()
        barcodes = decode(frame)
        
        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            return barcode_data
        
        cv2.imshow('Barcode Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None
