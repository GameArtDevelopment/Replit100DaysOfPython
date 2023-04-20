import os
import time

# define the file path for saving orders
ordersFilePath = "pizzaOrders.txt"

# define the size options and their respective prices
sizeOptions = {
    "personal": 6.99,
    "medium": 8.99,
    "large": 12.99
}

# define the 2D list
pizzaOrders = []

# function to display the menu


def displayMenu():
    print("\033[32m=\033[0m"*25)
    print("* Pizza Ordering System *")
    print("\033[31m=\033[0m"*25)
    print("1. Add an order")
    print("2. View orders")
    print("3. Edit an order")
    print("4. Exit")

# function to add an order


def addOrder():
    print("\033[32m=\033[0m"*41)
    print("* Welcome to the Pizza Ordering System! *")
    print("\033[31m=\033[0m"*41)
    print()
    name = input("What's your name? ")
    print()
    print("Welcome, " + name + "!")
    while True:
        print("Size Options:")
        for size, price in sizeOptions.items():
            print(f"{size.capitalize()} (${price:.2f})")
        sizeInput = input(
            "What size would you like your pizzas to be? ").lower()

        # check if the size input is valid
        if sizeInput not in sizeOptions:
            print("Please enter a valid size option.")
            continue

        # try to convert the quantity input to an integer
        while True:
            quantityInput = input("How many pizzas would you like to order? ")
            try:
                quantity = int(quantityInput)
                break
            except ValueError:
                print("Please enter a valid integer for the quantity.")

        # calculate cost and store in 2D list
        cost = quantity * sizeOptions[sizeInput]
        pizzaOrders.append([name, quantity, sizeInput, cost])

        # save the orders to file
        with open(ordersFilePath, "w") as f:
            f.write(str(pizzaOrders))

        # break out of the loop
        break

    print("Order added successfully.")

# function to view orders


def viewOrders():
    print("\033[32m=\033[0m"*19)
    print("* Current Orders: *")
    print("\033[31m=\033[0m"*19)
    print()
    for order in pizzaOrders:
        print(
            f"{order[0]} ordered {order[1]} {order[2]} pizzas for ${order[3]:.2f}")
    print()
# function to edit an order


def editOrders():
    os.system('clear')
    viewOrders()
    name = input(
        "Enter the name of the customer whose order you want to edit: ")
    for order in pizzaOrders:
        if order[0].lower() == name.lower():
            while True:
                print(f"Current order: {order[1]} {order[2]} pizzas")
                print("Size Options:")
                for size, price in sizeOptions.items():
                    print(f"{size.capitalize()} (${price:.2f})")
                sizeInput = input(
                    "What size would you like to change the order to? ").lower()

                # check if the size input is valid
                if sizeInput not in sizeOptions:
                    print("Please enter a valid size option.")
                    continue

                # try to convert the quantity input to an integer
                while True:
                    quantityInput = input(
                        "How many pizzas would you like to order? ")
                    try:
                        quantity = int(quantityInput)
                        break
                    except ValueError:
                        print("Please enter a valid integer for the quantity.")

                # update the order and save to file
                order[1] = quantity
                order[2] = sizeInput
                order[3] = quantity * sizeOptions[sizeInput]
                with open(ordersFilePath, "w") as f:
                    f.write(str(pizzaOrders))

                # break out of the loop

                break

            print("Order updated successfully.")
            break
    else:
        print("No order found for that customer.")

# function to exit the program


def exitProgram():
    os.system('clear')
    print("Exiting program.")
    time.sleep(1)
    os.system('clear')
    print("Exiting program..")
    time.sleep(1)
    os.system('clear')
    print("Exiting program...")
    time.sleep(1)
    os.system('clear')
    print("\033[31mProgram closed.\033[0m")
    print()
    print("Thank you for using the Pizza Ordering System!")
    print()
    print(
        "Find me on Twitter: \033[34mhttps://twitter.com/EnjoyTh3Ride\033[0m for more Python projects!")
    time.sleep(3)
    exit()

# function to clear the screen


def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

# function to load the orders from file


def loadOrders():
    if os.path.exists(ordersFilePath):
        with open(ordersFilePath, "r") as f:
            orders = f.read()
            if orders:
                orders = orders.replace(
                    "[[", "").replace("]]", "").split("], [")
                for order in orders:
                    order = order.replace("'", "").split(", ")
                    order[1] = int(order[1])
                    order[3] = float(order[3])
                    pizzaOrders.append(order)


# load the orders from file
loadOrders()

# main function


def main():
    while True:
        # clear the screen
        clearScreen()

        # display the menu
        displayMenu()

        # get the user's choice
        choice = input("Enter your choice: ")

        # clear the screen
        clearScreen()

        # check the user's choice
        if choice == "1":
            addOrder()
        elif choice == "2":
            viewOrders()
        elif choice == "3":
            editOrders()
        elif choice == "4":
            exitProgram()
        else:
            print("Please enter a valid choice.")

        # wait for the user to press enter
        input("Press enter to continue...")
        print()


# call the main function
main()
