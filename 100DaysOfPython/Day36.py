import os
import time

nameList = []


def title():
    print()
    print("\033[35m===============\033[0m")
    print("  \033[33m\033[1m* ROLODEX *\033[0m")
    print("\033[35m===============\033[0m")


while True:
    print("\033[33m\033[1mWelcome to my ROLODEX!\033[0m")
    print()
    print("\033[34mPlease select an option:\033[0m")
    print()
    print("1. View my roloDex")
    print("2. Add a name to my rolodex")
    print("3. Erase the entire rolodex")
    print("\033[31m4. Quit\033[0m")
    print()

    choice = input("Enter your option (1-4): ")

    if choice == "1":
        title()
        for item in nameList:
            print(item)
        time.sleep(3)
        os.system("clear")

    elif choice == "2":
        title()
        for item in nameList:
            print(item)
        print()
        firstName = input('Enter the first name: ').strip().capitalize()
        lastName = input('Enter the last name: ').strip().capitalize()
        newName = f"{firstName} {lastName}"
        if newName in nameList:
            print()
            print("That name is already in the rolo-dex!")
            time.sleep(1)
            os.system("clear")
        else:
            nameList.append(newName)
            print()
            print("{} has been added to the rolo-dex.".format(newName))
            time.sleep(1)
            os.system("clear")

    elif choice == "3":
        print()
        title()
        for item in nameList:
            print(item)
        print()
        confirm = input(
            "Are you sure you want to erase the entire rolo-dex? (y/n) ")
        if confirm == "y":
            nameList.clear()
            print()
            print("The rolo-dex has been erased.")
            time.sleep(1)
            os.system("clear")
        else:
            print()
            print("No changes have been made.")
            time.sleep(1)
            os.system("clear")

    elif choice == "4":
        print()
        print("\033[31mGoodbye!\033[0m")
        break

    else:
        print()
        print("That is not a valid choice.")
        time.sleep(1)
        os.system("clear")
print()
print("Thank you for using my rolodex!")
print()
