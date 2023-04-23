import time
import os

backupFolder = 'backup'
todoFilename = 'todo.txt'


def saveTodoList(todoList):
    if not os.path.exists(backupFolder):
        os.makedirs(backupFolder)

    backup_filename = os.path.join(
        backupFolder, f'{time.time()}-{todoFilename}')
    with open(backup_filename, 'w') as f:
        for item in todoList:
            f.write(item + '\n')


def loadTodoList():
    if not os.path.exists(todoFilename):
        return []

    with open(todoFilename, 'r') as f:
        return f.read().splitlines()


def addItem(todoList):
    newItem = input('Enter a new item: ').title()
    todoList.append(newItem)
    print('Added:', newItem)
    time.sleep(1)


def editItem(todoList):
    print("This is your current to do list:")
    viewList(todoList)
    itemNum = int(input('Enter the number of the item to edit: '))
    if itemNum < 1 or itemNum > len(todoList):
        print('Invalid item number.')
        return

    newItem = input(f'Enter the new text for item {itemNum}: ').title()
    todoList[itemNum - 1] = newItem
    print('Updated:', newItem)
    time.sleep(1)


def viewList(todoList):
    if len(todoList) == 0:
        print('The to-do list is empty.')
    else:
        print('To-do list:')
        for i, item in enumerate(todoList):
            print(f'{i+1}. {item}')

    input('Press Enter to continue...')


def main():
    todoList = loadTodoList()
    # main loop
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[32m=\033[0m' * 23)
        print('* To-Do List w/BACKUP *')
        print('\033[33m=\033[0m' * 23)
        print()
        print('\nSelect an option:')
        print('1. Add item')
        print('2. Edit item')
        print('3. View list')
        print('4. Exit')
        print()
        choice = input('> ')

        if choice == '1':
            addItem(todoList)
        elif choice == '2':
            editItem(todoList)
        elif choice == '3':
            viewList(todoList)
        elif choice == '4':
            saveTodoList(todoList)
            print('Goodbye!')
            print()
            print('Thank you for using my To-Do List w/BACKUP')
            print()
            break
        else:
            print('Invalid choice.')


main()
