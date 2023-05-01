import tkinter as tk

answer = 0
lastnumber = 0
operator = ""

# Function to update the label with the current value


def updateLabel(value):
    global answer
    current = int(value)
    answer = answer * 10 + current
    label.config(text=str(answer))

# Function to handle operator buttons


def operatorChoice(op):
    global lastnumber, operator, answer
    if operator == "":
        lastnumber = answer
    else:
        calc()
    operator = op
    answer = 0

# Function to clear the label and global variables


def clear():
    global answer, lastnumber, operator
    answer = 0
    lastnumber = 0
    operator = ""
    label.config(text="0")

# Function to perform the calculation and update the label


def calc():
    global answer, lastnumber, operator
    if operator == "+":
        answer = lastnumber + answer
    elif operator == "-":
        answer = lastnumber - answer
    elif operator == "*":
        answer = lastnumber * answer
    elif operator == "/":
        answer = lastnumber / answer
    label.config(text=str(answer))
    lastnumber = answer
    answer = 0
    operator = ""


# Create the GUI
window = tk.Tk()
window.title("Calculator")

# Create the label for the current value
label = tk.Label(window, text="0", font=("Helvetica", 36))
label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the buttons for the numbers and operators
button1 = tk.Button(window, text="1", font=("Helvetica", 24),
                    command=lambda: updateLabel("1"))
button2 = tk.Button(window, text="2", font=("Helvetica", 24),
                    command=lambda: updateLabel("2"))
button3 = tk.Button(window, text="3", font=("Helvetica", 24),
                    command=lambda: updateLabel("3"))
button4 = tk.Button(window, text="4", font=("Helvetica", 24),
                    command=lambda: updateLabel("4"))
button5 = tk.Button(window, text="5", font=("Helvetica", 24),
                    command=lambda: updateLabel("5"))
button6 = tk.Button(window, text="6", font=("Helvetica", 24),
                    command=lambda: updateLabel("6"))
button7 = tk.Button(window, text="7", font=("Helvetica", 24),
                    command=lambda: updateLabel("7"))
button8 = tk.Button(window, text="8", font=("Helvetica", 24),
                    command=lambda: updateLabel("8"))
button9 = tk.Button(window, text="9", font=("Helvetica", 24),
                    command=lambda: updateLabel("9"))
button0 = tk.Button(window, text="0", font=("Helvetica", 24),
                    command=lambda: updateLabel("0"))
buttonPlus = tk.Button(window, text="+", font=("Helvetica", 24),
                       command=lambda: operatorChoice("+"))
buttonMinus = tk.Button(window, text="-", font=("Helvetica", 24),
                        command=lambda: operatorChoice("-"))
buttonMultiply = tk.Button(window, text="*", font=("Helvetica", 24),
                           command=lambda: operatorChoice("*"))
buttonDivide = tk.Button(window, text="/", font=("Helvetica", 24),
                         command=lambda: operatorChoice("/"))
buttonEquals = tk.Button(
    window, text="=", font=("Helvetica", 24), command=calc)
buttonClear = tk.Button(window, text="C", font=(
    "Helvetica", 24), command=clear)

# Place the buttons on the grid
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
buttonPlus.grid(row=1, column=3)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonMinus.grid(row=2, column=3)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
buttonMultiply.grid(row=3, column=3)
button0.grid(row=4, column=0)
buttonEquals.grid(row=4, column=1)
buttonClear.grid(row=4, column=2)
buttonDivide.grid(row=4, column=3)

# Run the GUI
window.mainloop()
