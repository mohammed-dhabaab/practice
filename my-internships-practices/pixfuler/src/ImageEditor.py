import cv2
import tkinter as tk
import sv_ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageEditor:
    def __init__(self, window):
        self.window = window
        self.window.title("Pixfuler")
        sv_ttk.use_dark_theme()


        # Build the grid:
        self.window.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
        self.window.rowconfigure((0, 2), weight = 1)
        self.window.rowconfigure(1, weight = 2)

        # Create the canvas to display the image
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.grid(row = 1, column = 2, padx = 20, pady = 20)

        # Create the components
        self.upload_button = tk.Button(self.window, text="Upload Image", command=self.upload_image)
        self.upload_button.grid(row = 0, column = 0)

        self.save_button = tk.Button(self.window, text="Save Image", command=self.save_image)
        self.save_button.grid(row = 0, column = 1, sticky = "w")

        self.resize_button = tk.Button(self.window, text="Resize", command=self.resize_image)
        self.resize_button.grid(row = 3, column = 0)

        self.rotate_button = tk.Button(self.window, text="Rotate", command=self.rotate_image)
        self.rotate_button.grid(row = 3, column = 1)

        self.flip_button = tk.Button(self.window, text="Flip", command=self.flip_image)
        self.flip_button.grid(row = 3, column = 3)

        self.crop_button = tk.Button(self.window, text="Crop", command=self.crop_image)
        self.crop_button.grid(row = 3, column = 5)

        self.blur_button = tk.Button(self.window, text="Blur", command=self.blur_image)
        self.blur_button.grid(row = 3, column = 4)

        # Initialize variables
        self.image_path = None
        self.image = None
        self.display_image = None

    def upload_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_path = file_path
            self.load_image()

    def load_image(self):
        if self.image_path:
            self.image = cv2.imread(self.image_path)
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            # Resize the image to fit within the canvas dimensions
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            image_width = self.image.shape[1]
            image_height = self.image.shape[0]
            scale = min(canvas_width / image_width, canvas_height / image_height)
            new_width = int(image_width * scale)
            new_height = int(image_height * scale)
            dim = (new_width, new_height)
            self.image = cv2.resize(self.image, dim)

            self.update_image()

    def update_image(self):
    # Convert the image array to a PhotoImage object
        self.photo_image = ImageTk.PhotoImage(image=Image.fromarray(self.image))

        # Update the canvas with the new image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

    def save_image(self):
        # Save the image to a new file at the location specified by the user
        if self.image_path and self.image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All Files", "*.*")])
        if file_path:
            cv2.imwrite(file_path, self.image)

    def resize_image(self):
        # Open a dialog to get the new width and height from the user
        new_width = tk.simpledialog.askinteger("Resize Image", "Enter the new width:")
        new_height = tk.simpledialog.askinteger("Resize Image", "Enter the new height:")
        if new_width and new_height:
            self.image = cv2.resize(self.image, (new_width, new_height))
            self.update_image()

    def rotate_image(self):
        # Open a dialog to get the rotation angle from the user
        angle = tk.simpledialog.askinteger("Rotate Image", "Enter the rotation angle:")
        if angle:
            rows, cols, _ = self.image.shape
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
            self.image = cv2.warpAffine(self.image, M, (cols, rows))
            self.update_image()

    def crop_image(self):
        # Open a dialog to get the crop coordinates from the user
        x = tk.simpledialog.askinteger("Crop Image", "Enter the x-coordinate of the top-left corner:")
        y = tk.simpledialog.askinteger("Crop Image", "Enter the y-coordinate of the top-left corner:")
        width = tk.simpledialog.askinteger("Crop Image", "Enter the width:")
        height = tk.simpledialog.askinteger("Crop Image", "Enter the height:")
        if x and y and width and height:
            self.image = self.image[y:y+height, x:x+width]
            self.update_image()

    def blur_image(self):
        # Open a dialog to get the blur kernel size from the user
        kernel_size = tk.simpledialog.askinteger("Blur Image", "Enter the kernel size:")
        if kernel_size:
            self.image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)
            self.update_image()

    def flip_image(self):
        if self.image is not None:
            # Create a menu to allow the user to select the flip direction
            menu = tk.Menu(self.window, tearoff=0)
            menu.add_command(label="Horizontal", command=lambda: self.do_flip(1))
            menu.add_command(label="Vertical", command=lambda: self.do_flip(0))
            menu.tk_popup(self.window.winfo_pointerx(), self.window.winfo_pointery())

    def do_flip(self, direction):
        if direction == 0:
            self.image = cv2.flip(self.image, 0)
        elif direction == 1:
            self.image = cv2.flip(self.image, 1)
        self.update_image()