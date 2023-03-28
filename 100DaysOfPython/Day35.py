import os
import time

toDoList = []


def title():
    print()
    print("\033[33m===============\033[0m")
    print("* To-Do List: *")
    print("\033[33m===============\033[0m")


while True:
    print("\033[34mWelcome to the To-Do List app!\033[0m")
    print()
    print("Please select an option:")
    print()
    print("1. View the To-Do List")
    print("2. Add an item to the To-Do List")
    print("3. Remove an item from the To-Do List")
    print("4. Edit an item on the To-Do List")
    print("5. Erase the entire To-Do List")
    print("\033[31m6. Quit\033[0m")
    print()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        title()
        for item in toDoList:
            print(item)
        time.sleep(3)
        os.system("clear")
    elif choice == "2":
        print()
        newItem = input("Enter the new item: ")
        if newItem in toDoList:
            print()
            print("That item is already on the To-Do List!")
            time.sleep(1)
            os.system("clear")
        else:
            toDoList.append(newItem)
            print()
            print("{} has been added to the To-Do List.".format(newItem))
            time.sleep(1)
            os.system("clear")

    elif choice == "3":
        title()
        for item in toDoList:
            print(item)
        print()
        itemToRemove = input("Enter the item to remove: ")
        if itemToRemove in toDoList:
            print()
            confirm = input(
                "Are you sure you want to remove {}? (y/n) ".format(itemToRemove))
            if confirm == "y":
                toDoList.remove(itemToRemove)
                print()
                print("{} has been removed from the To-Do List.".format(
                    itemToRemove))
                time.sleep(1)
                os.system("clear")
            else:
                print("{} has not been removed from the To-Do List.".format(
                    itemToRemove))
                time.sleep(1)
                os.system("clear")
        else:
            print()
            print("That item is not on the To-Do List!")
            time.sleep(1)
            os.system("clear")

    elif choice == "4":
        title()
        for item in toDoList:
            print(item)
        print()
        oldItem = input("Enter the item to edit: ")
        if oldItem in toDoList:
            print()
            newItem = input(
                "Enter the new item to replace {}: ".format(oldItem))

            index = toDoList.index(oldItem)
            toDoList[index] = newItem
            print()
            print("{} has been updated to {}.".format(oldItem, newItem))
            time.sleep(1)
            os.system("clear")
        else:
            print()
            print("That item is not on the To-Do List!")
            time.sleep(1)
            os.system("clear")

    elif choice == "5":
        title()
        for item in toDoList:
            print(item)
        print()
        confirm = input(
            "Are you sure you want to erase the entire To-Do List? (y/n) ")
        if confirm == "y":
            toDoList.clear()
            print()
            print("The To-Do List has been erased.")
            time.sleep(1)
            os.system("clear")
        else:
            print("The To-Do List has not been erased.")
            time.sleep(1)
            os.system("clear")

    elif choice == "6":
        print()
        print("Goodbye!")
        print()
        print("Thank you for using the To-Do List app!")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 6.")
        time.sleep(1)
        os.system("clear")
time.sleep(1)
os.system("clear")
