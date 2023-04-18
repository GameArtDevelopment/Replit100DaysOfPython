import os
import time
import pickle

toDoList = []

# Check if a saved to-do list exists and load it
if os.path.exists("toDoList.pickle"):
    with open("toDoList.pickle", "rb") as f:
        toDoList = pickle.load(f)

while True:
    print()
    print("\033[33m        Welcome to your to do list!\033[0m")
    print("-------------------------------------------")
    print("\nMENU")
    print("1. Add")
    print("2. View")
    print("3. Edit")
    print("4. Remove")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        os.system('clear')
        task = input("Enter your to do: ")
        dueDate = input("Enter your due date (MM-DD-YYYY format): ")
        priority = input("Enter your priority (high, medium, low): ")
        toDoList.append(
            {"task": task, "dueDate": dueDate, "priority": priority})
        print("To do added successfully!")

        # Save the updated to-do list
        with open("toDoList.pickle", "wb") as f:
            pickle.dump(toDoList, f)

    elif choice == '2':
        os.system('clear')
        print("Would you like to view all to dos or by priority?")
        print("1. View all to dos")
        print("2. View by priority")

        viewChoice = input("Enter your choice (1-2): ")

        if viewChoice == '1':
            os.system('clear')
            print("All to dos:")
            os.system('clear')
            time.sleep(1)
            print("\033[35mLoading..\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[36mLoading...\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[35mLoading....\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[36mLoading.....\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[35mLoading......\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[33mYour to dos:\033[0m")
            print("------------")
            for index, task in enumerate(toDoList):
                print(
                    f"{index+1}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
                print("-----------------------------------------------")

        elif viewChoice == '2':
            os.system('clear')
            priorityChoice = input(
                "Enter the priority you want to view (high, medium, low): ")
            matchingTasks = [
                task for task in toDoList if task['priority'] == priorityChoice]
            os.system('clear')
            time.sleep(1)
            print("\033[35mLoading.\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[36mLoading..\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[35mLoading...\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[36mLoading....\033[0m")
            time.sleep(.5)
            os.system('clear')

            print("\033[33mYour to dos:\033[0m")
            print("------------")
            for index, task in enumerate(matchingTasks):
                print(
                    f"{index+1}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
                print("-----------------------------------------------")

    elif choice == '3':
        os.system('clear')
        print("Which to do would you like to edit?")
        for index, task in enumerate(toDoList):
            print(
                f"{index+1}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
            print("-----------------------------------------------")

        editChoice = int(
            input("Enter the number of the to do you want to edit: "))
        os.system('clear')
        print("Which part of the to do would you like to edit?")
        print("1. Task")
        print("2. Due Date")
        print("3. Priority")

        editChoice2 = int(input("Enter your choice (1-3): "))

        if editChoice2 == 1:
            os.system('clear')
            new_task = input("Enter the new task: ")
            toDoList[editChoice-1]['task'] = new_task
            print("To do edited successfully!")

        elif editChoice2 == 2:
            os.system('clear')
            new_dueDate = input(
                "Enter the new due date (MM-DD-YYYY format): ")
            toDoList[editChoice-1]['dueDate'] = new_dueDate
            print("To do edited successfully!")

        elif editChoice2 == 3:
            os.system('clear')
            newPriority = input(
                "Enter the new priority (high, medium, low): ")
            toDoList[editChoice-1]['priority'] = newPriority
            print("To do edited successfully!")

        # Save the updated to-do list
        with open("toDoList.pickle", "wb") as f:
            pickle.dump(toDoList, f)

    elif choice == '4':
        os.system('clear')
        print("Which to do would you like to remove?")
        for index, task in enumerate(toDoList):
            print(
                f"{index+1}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
            print("-----------------------------------------------")

        removeChoice = int(
            input("Enter the number of the to do you want to remove: "))
        toDoList.pop(removeChoice-1)
        print("To do removed successfully!")

        # Save the updated to-do list
        with open("toDoList.pickle", "wb") as f:
            pickle.dump(toDoList, f)

    elif choice == '5':
        os.system('clear')
        print("Thank you for using your to do list!")
        break

    else:
        os.system('clear')
        print("Invalid choice. Please try again.")

    input("Press enter to continue...")
    os.system('clear')
print()
print("Thank you for using my to do list!")
print()
print(
    "Follow me on Twitter: \033[34mhttps://twitter.com/enjoyth3ride\033[0m for more projects like this!")
print()
