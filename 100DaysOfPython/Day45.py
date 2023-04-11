import os
import time
to_do_list = []

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
        due_date = input("Enter your due date (MM-DD-YYYY format): ")
        priority = input("Enter your priority (high, medium, low): ")
        to_do_list.append(
            {"task": task, "due_date": due_date, "priority": priority})
        print("To do added successfully!")

    elif choice == '2':
        os.system('clear')
        print("Would you like to view all to dos or by priority?")
        print("1. View all to dos")
        print("2. View by priority")

        view_choice = input("Enter your choice (1-2): ")

        if view_choice == '1':
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
            for index, task in enumerate(to_do_list):
                print(
                    f"{index+1}. Task: {task['task']} | Due Date: {task['due_date']} | Priority: {task['priority']}")
                print("-----------------------------------------------")

        elif view_choice == '2':
            os.system('clear')
            priorityChoice = input(
                "Enter the priority you want to view (high, medium, low): ")
            matching_tasks = [
                task for task in to_do_list if task['priority'] == priorityChoice]
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
            print(f"To dos with priority {priorityChoice}:")
            print()
            for index, task in enumerate(matching_tasks):
                print(
                    f"{index+1}. Task: {task['task']} | Due Date: {task['due_date']} | Priority: {task['priority']}")
                print("-----------------------------------------------")

    elif choice == '3':
        os.system('clear')
        for index, task in enumerate(to_do_list):
            print(
                f"{index+1}. Task: {task['task']} | Due Date: {task['due_date']} | Priority: {task['priority']}")
            print("-----------------------------------------------")
        task_choice = int(
            input("Enter the number of the to do you want to edit: "))
        print(
            f"Editing task: {to_do_list[task_choice-1]['task']} | Due Date: {to_do_list[task_choice-1]['due_date']} | Priority: {to_do_list[task_choice-1]['priority']}")
        task = input("Enter the new to do: ")
        due_date = input("Enter the new due date (MM-DD-YYYY format): ")
        priority = input("Enter the new priority (high, medium, low): ")
        to_do_list[task_choice-1] = {"task": task,
                                     "due_date": due_date, "priority": priority}
        os.system('clear')
        print("To do was edited successfully!")

    elif choice == '4':
        os.system('clear')
        for index, task in enumerate(to_do_list):
            print(
                f"{index+1}. Task: {task['task']} | Due Date: {task['due_date']} | Priority: {task['priority']}")
            print("-----------------------------------------------")
        task_choice = int(
            input("Enter the number of the to do you want to remove: "))
        print(
            f"Removing task: {to_do_list[task_choice-1]['task']} | Due Date: {to_do_list[task_choice-1]['due_date']} | Priority: {to_do_list[task_choice-1]['priority']}")
        del to_do_list[task_choice-1]
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
        print("To do removed successfully!")

    elif choice == '5':
        os.system('clear')
        print("\033[31mExiting program.\033[0m")
        time.sleep(1)
        os.system('clear')
        print("\033[35mExiting program..\033[0m")
        time.sleep(.5)
        os.system('clear')
        print("\033[36mExiting program..\033[0m")
        time.sleep(.5)
        os.system('clear')
        print("\033[35mExiting program...\033[0m")
        time.sleep(.5)
        os.system('clear')
        print("\033[33mExiting program...\033[0m")
        time.sleep(.7)
        os.system('clear')
        print("\033[35mExiting program....\033[0m")
        time.sleep(1)
        os.system('clear')
        print("\033[31mExiting program....\033[0m")
        time.sleep(1)
        os.system('clear')
        print("\033[31mProgram exited successfully!\033[0m")
        print()
        break

    else:
        print("Invalid input. Please enter a number from 1-5.")
