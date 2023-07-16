import os
from PIL import Image

# Set the paths for the input and output directories
input_dir = "rawdata"
output_dir = "dogData"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Loop through all the files in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a JPG image
    if filename.endswith(".jpg"):
        # Open the JPG image and convert it to BMP format
        jpg_image = Image.open(os.path.join(input_dir, filename))
        bmp_image = jpg_image.convert("RGB")
        
        # Save the BMP image to the output directory with the same filename
        bmp_filename = os.path.splitext(filename)[0] + ".bmp"
        bmp_image.save(os.path.join(output_dir, bmp_filename))