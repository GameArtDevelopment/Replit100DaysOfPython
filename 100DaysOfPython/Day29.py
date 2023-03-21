import os
import time
play = "yes"


def superSub(word, color):
    if color == "red":
        print("\033[31m", word, sep="", end="")
    elif color == "yellow":
        print("\033[33m", word, sep="", end="")
    elif color == "green":
        print("\033[32m", word, sep="", end="")
    elif color == "blue":
        print("\033[34m", word, sep="", end="")
    else:
        print("\033[0m", word, sep="")


while play == "yes":
    print("\033[?25l", end="")
    time.sleep(1)
    superSub("        **** Super Subroutine ****", "red")
    print()
    time.sleep(1)
    superSub("Secret Print Functions -", "")
    superSub("With my new program", "yellow")
    time.sleep(1)
    superSub(" I can just call red('and') ", "")
    time.sleep(1)
    superSub("it will print in red ", "red")
    print()
    time.sleep(2)
    superSub("or even green", "green")
    print()
    time.sleep(3)
    superSub("And with time.sleep(5),it delayed words", "")
    time.sleep(5)
    print("5 seconds.")
    time.sleep(1.5)
    print()
    print("\033[?25h", end="")
    play = input("Play Again?: ")
    os.system("clear")
