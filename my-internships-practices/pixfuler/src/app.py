import image_processing as img_pro
import cv2


# if __name__ == '__main__':


import tkinter as tk
from tkinter import ttk
import sv_ttk


# Frame setup:
root = tk.Tk()
sv_ttk.use_dark_theme()
root.title("My Interface")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


# Components:
button = ttk.Button(root, text="Button")
button.pack()

ttk.Combobox().pack()
ttk.Menubutton().pack()
ttk.Frame().pack()

# Toggle button between themes
button = ttk.Button(root, text="Toggle theme", command = sv_ttk.toggle_theme)
button.pack()



sv_ttk.set_theme("dark")
root.mainloop()


# Image procceing usage:
# image_path = img_pro.get_image_path()
# image = cv2.imread(image_path)

# img_pro.display_image(image)