import cv2
import tkinter as tk
from tkinter import filedialog
import os

# Create a Tkinter root window to open a directory dialog
root = tk.Tk()
root.withdraw()

# Open a directory dialog to select a folder to save the output images
output_dir = filedialog.askdirectory()

# Open a file dialog to select one or more image files
file_paths = filedialog.askopenfilenames()

# Loop over the selected file paths
for file_path in file_paths:
    # Load the input image file
    img = cv2.imread(file_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a new file name for the grayscale image
    file_name, file_ext = os.path.splitext(os.path.basename(file_path))
    gray_file_path = os.path.join(output_dir, file_name + '_gray' + file_ext)

    # Save the grayscale image as a new file
    cv2.imwrite(gray_file_path, gray)