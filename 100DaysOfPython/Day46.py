import os
import time

prezbeasts = []

typeColor = {
    "Earth": "\033[32m",
    "Wind": "\033[33m",
    "Fire": "\033[31m",
    "Water": "\033[34m",
    "Heart": "\033[35m"
}


def addPrezBeast():
    os.system("clear")
    print("Add PrezBeast\n")
    prezdex = {
        "Beast Name": "",
        "Type": "",
        "Special Move": "",
        "HP": "",
        "MP": ""
    }
    for key in prezdex:
        prezdex[key] = input(f"{key}: ").strip().title()
    prezbeasts.append(prezdex)
    os.system('clear')
    time.sleep(1)
    print("\033[32mAddingBeast..\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[33mAddingBeast...\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[32mAddingBeast....\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[33mAddingBeast.....\033[0m")
    time.sleep(.5)
    os.system('clear')
    input("\nPrezBeast added. Press Enter to continue.")


def editPrezBeast():
    os.system("clear")
    print("Edit PrezBeast\n")
    if not prezbeasts:
        print("There are no PrezBeasts to edit.")
        input("Press Enter to continue.")
        return

    prezCount = 1
    for prez in prezbeasts:
        print(f"\nPrezBeast {prezCount}")
        prezCount += 1
        for key, value in prez.items():
            if key == "Type":
                print(f"{key}: {typeColor[value]}{value}\033[0m")
            else:
                print(f"{key}: {value}")

    beastNum = int(input("Enter the number of the PrezBeast to edit: "))
    if beastNum < 1 or beastNum > len(prezbeasts):
        print("Invalid PrezBeast number.")
        input("Press Enter to continue.")
        return

    prezdex = prezbeasts[beastNum - 1]
    print(f"\nPrezBeast {beastNum}")
    for key, value in prezdex.items():
        print(f"{key}: {value}")

    print("\nWhat do you want to edit?")
    key = input("Enter the attribute to edit: ")
    if key not in prezdex:
        print("Invalid key.")
        input("Press Enter to continue.")
        return

    value = input(f"Enter the new value for {key}: ").strip().title()
    prezdex[key] = value

    input("\nPrezBeast edited. Press Enter to continue.")
    os.system('clear')


def viewPrezBeast():
    os.system('clear')
    time.sleep(1)
    print("\033[32mLoading.\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[33mPrezBeast..\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[32mLoading..\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[33mPrezBeast...\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[32mLoading...\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[33mPrezBeast....\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[32mLoading.....\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("View PrezBeast\n")
    if not prezbeasts:
        print("There are no PrezBeasts to view.")
        input("Press Enter to continue.")
        return
    prezCount = 1
    for prezdex in prezbeasts:
        print(f"\nPrezBeast {prezCount}")
        prezCount += 1
        for key in prezdex:
            if key == "Type":
                print(f"{key}: {typeColor[prezdex[key]]}{prezdex[key]}\033[0m")
            else:
                print(f"{key}: {prezdex[key]}")

    input("\nPress Enter to continue.")


def removePrezBeast():
    os.system("clear")
    print("Remove PrezBeast\n")
    if not prezbeasts:
        print("There are no PrezBeasts to remove.")
        input("Press Enter to continue.")
        return
    prezCount = 1
    for prezdex in prezbeasts:
        print(f"\nPrezBeast {prezCount}")
        for key in prezdex.keys():
            value = prezdex[key]
            if key == "Type":
                print(f"{key}: {typeColor[value]}{value}\033[0m")
            else:
                print(f"{key}: {value}")
    prezCount += 1

    beastNum = int(input("Enter the number of the PrezBeast to remove: "))
    if beastNum < 1 or beastNum > len(prezbeasts):
        print("Invalid PrezBeast number.")
        input("Press Enter to continue.")
        return
    del prezbeasts[beastNum - 1]
    input("\nPrezBeast removed. Press Enter to continue.")


def main():
    os.system("clear")
    print("\033[36m=====================================\033[0m")
    print("*   Welcome to the PrezBeast App!   *")
    print("\033[34m=====================================\033[0m")
    while True:
        print("1. Add a PrezBeast")
        print("2. Edit a PrezBeast")
        print("3. View all PrezBeasts")
        print("4. Remove a PrezBeast")
        print("5. Exit the program")
        print()
        choice = input("Enter a number to make a choice: ")
        if choice == "1":
            addPrezBeast()
        elif choice == "2":
            editPrezBeast()
        elif choice == "3":
            viewPrezBeast()
        elif choice == "4":
            removePrezBeast()
        elif choice == "5":
            break
        else:
            print()
            print("Invalid choice. Please try again.")
            print()
            input("Press Enter to continue.")
    os.system('clear')
    time.sleep(1)
    print("\033[31mExiting.\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[35mExiting..\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[31mExiting...\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[35mExiting....\033[0m")
    time.sleep(.5)
    os.system('clear')
    print("\033[31mExiting.....\033[0m")
    time.sleep(.5)
    os.system('clear')
    print()
    print("Thank you for using my PrezBeast App.")
    print()
    print("I hope you enjoyed it.")
    print()
    print(
        "Follow me on twitter \033[34mhttps://twitter.com/EnjoyTh3Ride\033[0m")
    print()


main()
