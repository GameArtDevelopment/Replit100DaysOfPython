import tkinter as tk
from PIL import ImageTk, Image
import os

# Set up the window
window = tk.Tk()
window.geometry('500x400')

# Define a function to find the image


def find_image():
    name = name_entry.get()
    image_path = f'100DaysOfPython/GuessWho/{name}.png'
    if os.path.isfile(image_path):
        # Load and display the image
        image = Image.open(image_path)
        image = image.resize((400, 300))
        image = ImageTk.PhotoImage(image)
        canvas.create_image(50, 0, anchor='nw', image=image)
        canvas.image = image
        error_label.pack_forget()
        canvas.pack()
    else:
        # Show error message
        error_label.pack()
        canvas.pack_forget()


# Set up the label, entry, and button widgets
name_label = tk.Label(window, text='Guess What?')
name_entry = tk.Entry(window)
find_button = tk.Button(window, text='Find', command=find_image)

# Set up the canvas and error label widgets
canvas = tk.Canvas(window, width=500, height=400)
error_label = tk.Label(
    window, text="Unable to find image\nTry 'Pandas', 'Pygame', 'Python' or 'Tkinter'")

# Pack the widgets
name_label.pack()
name_entry.pack()
find_button.pack()
error_label.pack_forget()
canvas.pack()

# Start the main loop
window.mainloop()
