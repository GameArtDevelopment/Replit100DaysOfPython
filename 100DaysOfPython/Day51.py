import os
import time

toDoList = []

# Check if a saved to-do list exists and load it
if os.path.exists("toDoList.txt"):
    with open("toDoList.txt", "r") as f:
        file_contents = f.read()
        if file_contents:
            toDoList = eval(file_contents)

while True:
    print()
    print("\033[33m        Welcome to your to do list!\033[0m")
    print("\033[32m-----------------------------------------------\033[0m")
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
        with open("toDoList.txt", "w") as f:
            f.write(str(toDoList))

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
            index = 0
            for task in toDoList:
                index += 1
                print(
                    f"{index}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
                print(
                    "\033[35m-----------------------------------------------\033[0m")

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
            print("\033[35mLoading.....\033[0m")
            time.sleep(.5)
            os.system('clear')
            print("\033[33mYour to dos:\033[0m")
            print("------------")
            index = 0
            for task in toDoList:
                index += 1
                print(
                    f"{index}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
                print(
                    "\033[35m-----------------------------------------------\033[0m")

    elif choice == '3':
        os.system('clear')
        print("Would you like to edit a task or due date?")
        print("1. Edit task")
        print("2. Edit due date")

        editChoice = input("Enter your choice (1-2): ")

        if editChoice == '1':
            os.system('clear')
            print("\033[33mYour updated to do list:\033[0m")
            print("------------")
            index = 0
            for task in toDoList:
                index += 1
                print(
                    f"{index}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
                print(
                    "\033[35m-----------------------------------------------\033[0m")

            taskNumber = int(
                input("Enter the number of the task you want to edit: "))
            newTask = input("Enter the new task: ")
            toDoList[taskNumber-1]['task'] = newTask
            print("Task edited successfully!")

            # Save the updated to-do list
            with open("toDoList.txt", "w") as f:
                f.write(str(toDoList))

        elif editChoice == '2':
            os.system('clear')
            print("\033[33mYour updated to do list:\033[0m")
            print("------------")
            index = 0
            for task in toDoList:
                index += 1
                print(
                    f"{index}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
                print(
                    "\033[34m-----------------------------------------------\033[0m")
            taskNumber = int(
                input("Enter the number of the task you want to edit: "))
            newDueDate = input("Enter the new due date: ")
            toDoList[taskNumber-1]['dueDate'] = newDueDate
            print("Due date edited successfully!")

            # Save the updated to-do list
            with open("toDoList.txt", "w") as f:
                f.write(str(toDoList))

    elif choice == '4':
        os.system('clear')
        print("\033[33mYour updated to do list:\033[0m")
        print("------------")
        index = 0
        for task in toDoList:
            index += 1
            print(
                f"{index}. Task: {task['task']} | Due Date: {task['dueDate']} | Priority: {task['priority']}")
            print(
                "\033[36m-----------------------------------------------\033[0m")
        taskNumber = int(
            input("Enter the number of the task you want to remove: "))
        toDoList.pop(taskNumber-1)
        print("Task removed successfully!")

        # Save the updated to-do list
        with open("toDoList.txt", "w") as f:
            f.write(str(toDoList))

    elif choice == '5':
        os.system('clear')
        os.system('clear')
        time.sleep(1)
        print("\033[33mSaving.\033[0m")
        time.sleep(.5)
        os.system('clear')
        print("\033[32mSaving..\033[0m")
        time.sleep(.5)
        os.system('clear')
        print("\033[33mSaving...\033[0m")
        time.sleep(.5)
        os.system('clear')
        print("\033[32mSaving....\033[0m")
        time.sleep(.5)
        os.system('clear')
        print()
        print("Your To Do List has been saved!")
        print()
        print("Thank you for using my to do list!")
        print()
        print(
            "Follow me on twitter \033[34mhttps://twitter.com/EnjoyTh3Ride\033[0m for more projects!")
        break

    else:
        os.system('clear')
        print("Invalid choice!")

    input("Press Enter to continue...")
    os.system('clear')
