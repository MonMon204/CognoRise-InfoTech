#
#    Task7_QRCodeEncoderDecoder.py
#
# Created on Fri Aug 23 2024 12:58:24 AM
#       Author: Mina Waguih
#
# Description: A simple QR code encoder and decoder
#


# Encoder

import qrcode

def generate_qr_code(data, filename):
    """
    Generate a QR code for the given data and save it to a file.

    Args:
        data (str): The data to encode (e.g. URL, text, etc.)
        filename (str): The filename to save the QR code image as
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    if not filename.endswith(".png") or not filename.endswith(".jpg") or not filename.endswith(".jpeg"):
        filename += ".png"
    
    img.save(filename)

    # Example usage:
    # data = "https://www.example.com"
    # filename = "qr_code.png"
    # generate_qr_code(data, filename)


# Decoder

import cv2
import pyzbar.pyzbar as pyzbar

def decode_qr_code(image_path):
    """
    Decode a QR code from an image file.

    Args:
        image_path (str): The path to the image file containing the QR code

    Returns:
        str: The decoded data from the QR code
    """

    image = cv2.imread(image_path)
    decoded_objects = pyzbar.decode(image)

    for obj in decoded_objects:
        return obj.data.decode("utf-8")

    # Example usage:
    # image_path = "qr_code.png"
    # decoded_data = decode_qr_code(image_path)
    # print("Decoded data:", decoded_data)

print("*********** QRcode ***********")
choice = int(input("1-Encode\n2-Decode\n Choose (1-2): "))

if choice == 1:
    data = input("Enter your data to encode: ")
    filename = input("Enter the QRcode image file name: ")
    generate_qr_code(data,filename)

elif choice == 2:
    imagepath = str(input("Enter QRcode image path: "))
    if imagepath.endswith(".png") or imagepath.endswith(".jpg") or imagepath.endswith(".jpeg"):
        print("Decoded data:",decode_qr_code(imagepath))
    
    else:
        print("Invalid Image Path!!")

else:
    print("Invalid Choice!!")