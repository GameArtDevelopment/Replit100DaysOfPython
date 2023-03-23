import os
import time


def addColor(color):
    if color == "red":
        return ("\033[31m")
    elif color == "yellow":
        return ("\033[33m")
    elif color == "green":
        return ("\033[32m")
    elif color == "blue":
        return ("\033[34m")
    elif color == "pink":
        return ("\033[35m")
    elif color == "white":
        return ("\033[0m")


title = f"{addColor('red')}={addColor('white')}={addColor('blue')}={addColor('yellow')} MUSIC APP {addColor('blue')}={addColor('white')}={addColor('red')}="
play = f"▶️{addColor('white')} Radio Gaga"
author = f"\t👸{addColor('yellow')}QUEEN"

prev = f"{addColor('white')} PREV"
next = f"{addColor('green')} NEXT"
pause = f"{addColor('pink')} PAUSE"

print(f"       {title}")
print()
print(play)
print()
print(author)
print()
print(prev, end="  \v")
print(next, end="  \v")
print(pause, end="  \v")
print()
lines = "------------------------------------"
print(f"{addColor('red')}{lines:^35}")
print()
print(f"{addColor('white')}          WELCOME TO")
name = "--   ARMBOOK   --"
print(f"{addColor('blue')}{name:^30}")
print()
print(f"\t{addColor('yellow')}   Definitely not a rip off of")
text = "a certain other social"
print(f"{addColor('yellow')}{text:>38}")
lastText = "networking site"
print(f"{addColor('yellow')}{lastText:>38}")
print()
honest = "HONEST!"
print(f"{addColor('red')}{honest:^30}")
print()
user = "Username:"
print(f"{addColor('white')}{user:^30}")
passWord = "Password:"
print(f"{addColor('white')}{passWord:^30}")
print()
print("Thank you for trying my code. I appreciate your support!")
