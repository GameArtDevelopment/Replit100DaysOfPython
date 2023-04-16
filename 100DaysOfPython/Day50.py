import os
import time
import random


def menu():
    while True:
        os.system('clear')
        print("\033[33m=\033[0m" * 37)
        print("*   Welcome to the idea generator   *")
        print("\033[34m=\033[0m" * 37)
        print()
        print("1. Add an idea")
        print("2. Load random")
        print("3. \033[31mExit\033[0m")
        print()
        choice = input("Enter your choice: ")
        if choice == '1':
            addIdea()
        elif choice == '2':
            os.system('clear')
            loadRandomIdea()
        elif choice == '3':
            os.system('clear')
            print("\033[31mExiting.\033[0m")
            time.sleep(1)
            os.system('clear')
            print("\033[36mExiting..\033[0m")
            time.sleep(1)
            os.system('clear')
            print("\033[31mExiting...\033[0m")
            time.sleep(1)
            os.system('clear')
            break
        else:
            print("Invalid choice")


def addIdea():
    idea = input("Enter your idea: ").capitalize()
    with open('my.ideas', 'a') as f:
        f.write(idea + '\n')
    print("Idea added successfully")
    time.sleep(1)


def loadRandomIdea():
    print("\033[32mLoading random idea.\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[35mLoading random idea..\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[36mLoading random idea...\033[0m")
    time.sleep(1)
    os.system('clear')
    try:
        with open('my.ideas', 'r') as f:
            ideas = f.read().splitlines()
    except FileNotFoundError:
        print("No ideas found")
        time.sleep(2)
        return

    randomIdea = random.choice(ideas)
    print(randomIdea)
    time.sleep(2)


menu()

print("Thank you for using my idea generator")
print()
print(
    "Follow me on twitter: \033[34mhttps://twitter.com/EnjoyTh3Ride\033[0m for more projects like this one")
print()
