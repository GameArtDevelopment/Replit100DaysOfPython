import random
import os
import time
totalAttempts = 0


def game():
    attempts = 0
    number = random.randint(1, 10)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        guess = int(input("Pick a number between 1 and 10: "))
        if guess > number:
            print("Too high")
            time.sleep(1)
            attempts += 1
        elif guess < number:
            print("Too low")
            time.sleep(1)
            attempts += 1
        else:
            print("Just right!")
            print(
                f"\033[33m{attempts}\033[0m \033[36mattempts this round\033[0m")
            time.sleep(3)
            return attempts


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[33m=\033[0m" * 43)
    print("* Guess the number game. DEBUGGED EDITION *")
    print("\033[36m=\033[0m" * 43)
    menu = input(
        "1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
    if int(menu) == 1:
        totalAttempts += game()
    elif menu == '2':
        print(
            f"\033[36mYou've had a total of \033[0m\033[33m{totalAttempts}\033[0m \033[36mattempts\033[0m")
        time.sleep(3)
    elif menu == '3':
        break
