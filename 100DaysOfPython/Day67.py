import tkinter as tk
from PIL import Image, ImageTk

# create a Tkinter window
window = tk.Tk()
window.title("Guess What?")
window.geometry("400x400")

# create a label
label = tk.Label(text="Guess What?")
label.pack()

# create a text input
text = tk.Entry(window, width=30)
text.pack()

# create a button and define its command


def show_image():
    item = text.get().lower().strip()
    images = {
        "pandas": "Pandas.png",
        "pygame": "Pygame.png",
        "python": "Python.png",
        "tkinter": "Tkinter.png"
    }
    if item in images:
        image_path = "100DaysOfPython/GuessWho/" + images[item]
        image = ImageTk.PhotoImage(Image.open(image_path))
        canvas.itemconfig(container, image=image)
        canvas.image = image
    else:
        label.config(text="Try 'pandas', 'pygame', 'python' or 'tkinter'")


button = tk.Button(text="Find", command=show_image)
button.pack()

# create a canvas to display the image
canvas = tk.Canvas(window, width=400, height=380)
canvas.pack()

# set a default image
python_image = ImageTk.PhotoImage(
    Image.open("100DaysOfPython/GuessWho/Python.png"))
container = canvas.create_image(200, 100, image=python_image)
# run the main loop
tk.mainloop()
