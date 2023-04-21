import os
import os.path

# Define the file name to store the inventory data
fileName = "inventory.txt"

# Create the file if it doesn't exist
if not os.path.exists(fileName):
    with open(fileName, 'w'):
        pass

# Function to add an item to the inventory


def addItem():
    itemName = input("Enter item name: ").capitalize()
    with open(fileName, 'a') as f:
        f.write(itemName + "\n")
    clearScreen()
    print(f"{itemName} added to inventory")

# Function to remove an item from the inventory


def removeItem():
    itemName = input("Enter item name to remove: ").capitalize()
    with open(fileName, 'r') as f:
        items = [line.strip() for line in f.readlines()]
    with open(fileName, 'w') as f:
        removed = False
        for item in items:
            if item == itemName and not removed:
                removed = True
            else:
                f.write(item + "\n")
        if removed:
            clearScreen()
            print(f"{itemName} removed from inventory")
        else:
            clearScreen()
            print(f"{itemName} not found in inventory")

# Function to view the inventory


def viewInventory():
    with open(fileName, 'r') as f:
        items = [line.strip() for line in f.readlines()]
    inventory = {}
    for item in items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    if inventory:
        clearScreen()
        print("Inventory:")
        print("=" * 10)
        for item, count in inventory.items():
            print(f"{item}: {count}")
    else:
        clearScreen()
        print("Inventory is empty")

# Function to clear the screen


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main menu
while True:
    print("=" * 30)
    print("* \033[30mBarbarian Inventory System\033[0m *")
    print("=" * 30)
    print()
    print("1. Add item")
    print("2. Remove item")
    print("3. View inventory")
    print("4. \033[31mExit\033[0m")
    choice = input("Enter your choice: ")

    try:
        choice = int(choice)
        if choice == 1:
            addItem()
        elif choice == 2:
            removeItem()
        elif choice == 3:
            viewInventory()
        elif choice == 4:
            break
        else:
            clearScreen()
            print("Invalid choice")
    except ValueError:
        clearScreen()
        print("Invalid choice")
