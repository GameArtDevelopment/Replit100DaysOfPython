import myLibrary as lib
import os
import time


while True:
    os.system("clear")
    print("\033[32m=\033[0m"*31)
    print("** Welcome to my sub-library **")
    print("\033[36m=\033[0m"*31)
    print()
    print("         MENU")
    print("1. Generation generator")
    print("2. Number Guessing Game")
    print("3. Interest Calculator")
    print("4. Dice Roller")
    print("5. To Do List")
    print("6. \033[31mExit\033[0m")
    print()
    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        lib.generationGenerator()
    elif choice == 2:
        lib.numGuess()
    elif choice == 3:
        lib.interestCalc()
    elif choice == 4:
        lib.diceRoll()
    elif choice == 5:
        lib.toDoList()
    elif choice == 6:
        print("Thank you for trying my sub-library.")
        print()
        break
    else:
        print("\033[31mInvalid choice. Please choose again.\033[0m")
        time.sleep(1)
