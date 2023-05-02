import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Visual Novel")
window.geometry("400x400")

story = "What is the best programming language?"


def iCode():
    global story
    canvas.itemconfig(container, image=codes)
    story = "I want to learn it all, but I don't know where to start!"
    storyLabel.config(text=story)
    button.pack_forget()
    button2.pack_forget()
    button3.pack()
    button4.pack()


def iReplit():
    global story
    canvas.itemconfig(container, image=replit)
    story = "Is Python is the best language to start with?"
    storyLabel.config(text=story)
    button.pack_forget()
    button2.pack_forget()
    button5.pack()
    button6.pack()


def iEdit():
    global story
    canvas.itemconfig(container, image=vs)
    story = "She's not into video games\nBYE!"
    storyLabel.config(text=story)
    button3.pack_forget()
    button4.pack_forget()
    restartButton.pack()


def iUse():
    global story
    canvas.itemconfig(container, image=amazing)
    story = "She agrees with you\n and decide to go on the python path together."
    storyLabel.config(text=story)
    button3.pack_forget()
    button4.pack_forget()
    restartButton.pack()


def iToo():
    global story
    canvas.itemconfig(container, image=days)
    story = "She tells you how Javascript can do it all!\nand leaves."
    storyLabel.config(text=story)
    button5.pack_forget()
    button6.pack_forget()
    restartButton.pack()


def iWin():
    global story
    canvas.itemconfig(container, image=amazing)
    story = "That's Great!\n Python is an amazing first language\nlet's go through the python path together."
    storyLabel.config(text=story)
    button5.pack_forget()
    button6.pack_forget()
    restartButton.pack()


def restart():
    global story
    canvas.itemconfig(container, image=start)
    story = "What is the best programming language?"
    storyLabel.config(text=story)
    restartButton.pack_forget()
    button.pack()
    button2.pack()


# Load images
start = tk.PhotoImage(
    file="100DaysOfPython/TextAdventure/page1.png").subsample(4)
codes = tk.PhotoImage(
    file="100DaysOfPython/TextAdventure/page2a.png").subsample(4)
replit = tk.PhotoImage(
    file="100DaysOfPython/TextAdventure/page2b.png").subsample(4)
days = tk.PhotoImage(
    file="100DaysOfPython/TextAdventure/page3a.png").subsample(4)
amazing = tk.PhotoImage(
    file="100DaysOfPython/TextAdventure/page3b.png").subsample(4)
vs = tk.PhotoImage(
    file="100DaysOfPython/TextAdventure/page4a.png").subsample(4)

# Create the canvas to display the images
canvas = tk.Canvas(window, width=400, height=300)
container = canvas.create_image(200, 150, image=start)
canvas.pack()

# Create the story label
storyLabel = tk.Label(window, text=story, font=("Helvetica", 16))
storyLabel.pack()

# Create the buttons
button = tk.Button(window, text="What do you want to learn?", command=iCode)
button2 = tk.Button(window, text="Have you heard of Python?", command=iReplit)
button3 = tk.Button(
    window, text="How about C#?", command=iEdit)
button4 = tk.Button(window, text="How about Python?", command=iUse)
button5 = tk.Button(window, text="I prefer Javascript", command=iToo)
button6 = tk.Button(
    window, text="Learn Python first", command=iWin)
restartButton = tk.Button(window, text="Restart", command=restart)

# Add the buttons to the window
button.pack()
button2.pack()

# Start the GUI
window.mainloop()
