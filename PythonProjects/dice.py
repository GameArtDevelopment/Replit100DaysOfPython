import os
import time
import random
print("========================================")
print("      Welcome to my Dice Roller!")
print("========================================")
print()
while True:
    rollAgain = input(
        "Would you like to roll the dice? (y/n): ").strip().lower()
    if rollAgain == "n":
        break
    elif rollAgain == "y":
        dice = int(input("How many dice would you like to roll? "))
        print()
        print("Rolling the dice...")
        print()
        time.sleep(1)
        os.system("clear")
        print("The dice rolled a {}.".format(random.randint(1, 6)))
        print()
print()
print("Thank you for using my Dice Roller!")
print()
