import os
import time
line = ("\033[31m=======================\033[0m")
title = ("*     To Do List      *")
toDoList = []


def printList():
    print(f"\n{line}\n{title}\n{line}")
    for item in toDoList:
        print(item)
    print(line)


def addToList():
    item = input("\nWhat task would you like to add?: ")
    toDoList.append(item)
    print(f"\n'{item}' has been added to your list.\n")
    time.sleep(2)


def editList():
    if not toDoList:
        print("\nYour list is empty.\n")
        return
    print("\nHere is your current list:")
    printList()
    item = input("\nWhich item would you like to remove?: ")
    if item in toDoList:
        toDoList.remove(item)
        print(f"\n'{item}' has been removed from your list.\n")
        time.sleep(2)
    else:
        print(f"\n'{item}' was not found in your list.\n")
        time.sleep(2)


while True:
    os.system("clear")
    printList()
    action = input(
        "\n\033[34mWhat would you like to do?: \033[0m(view / add / edit / quit)\n ")
    if action == "view":
        printList()
        time.sleep(2)
    elif action == "add":
        addToList()
    elif action == "edit":
        editList()
    elif action == "quit":
        print("\nGoodbye!\n")
        print("\nThank you for trying my simple ToDoList.\n")
        break
    else:
        print("\n\033[33mInvalid input. Please try again.\033[0m\n")
        time.sleep(2)
