import os
import time
print(" ========================================")
print("Welcome to the Odd or Even Number Checker!")
print(" ========================================")
print()
attempts = 0
tryAgain = "y"
while True:
    if attempts > 0:
        tryAgain = input(
            "Would you like to check another number? (y/n): ").strip().lower()
    if tryAgain == "n":
        break
    elif attempts == 0 or tryAgain == "y":
        time.sleep(1)
        os.system("clear")
        number = int(input("Enter a number: "))
        attempts += 1
        if number % 2 == 0:
            print("This is an even number.")
            print()
        elif number < 0 and number % 2 == 0:
            print("This is a negative even number.")
            print()
        elif number < 0 and number % 2 == 1:
            print("This is a negative odd number.")
            print()
        else:
            print("This is an odd number.")
            print()
print()
print("Thank you for using my Odd or Even Number Checker!")
print()
