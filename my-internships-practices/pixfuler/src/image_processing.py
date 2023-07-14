import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np


def get_image_path():
    # Create Tkinter root window (needed for file dialog)
    root = Tk()
    root.withdraw() # Hide the root window

    # Open file dialog to select an image file
    image_path = askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    
    return image_path

def display_image(image):
    # Display the image
    cv2.imshow('Image', image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize_image(image, width, height):
    new_width = image.shape[1] * width
    new_height = image.shape[0] * height
    # Resize the image
    resized_image = cv2.resize(image, (int(new_width), int(new_height)))

    return resized_image

def rotate_image(image, angle):
    height, width = image.shape[:2]

    # Calculate rotation matrix
    M = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)

    # Apply rotation to image
    rotated_image = cv2.warpAffine(image, M, (width, height))

    return rotated_image

def flip_image_horizontally(image):
    # Flip image horizontally
    flipped_img_horizontal = cv2.flip(image, 1)
    
    return flip_image_horizontally

def flip_image_horizontally(image):
    # Flip image vertically
    flipped_img_vertical = cv2.flip(image, 0)

    return flipped_img_vertical

def blur_image(image, ksize):
    # `ksize` is the kernel size for blurring. A larger kernel size will result in a stronger blur effect.
    blurred_image = cv2.blur(image, (ksize, ksize))

    return blurred_image

def crop_image(image, x_start, y_start, x_end, y_end):
    cropped_image = image[y_start:y_end, x_start:x_end]

    return cropped_image

# # Check if the image was loaded successfully
# if image is not None:
#     print('Image was loaded successfully')
# else:
#     # Failed to load the image
#     print('Failed to load image file')