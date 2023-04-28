import os
import time
from datetime import datetime

# Set the password
passWord = "password123"

# Define the diary database filename
diaryFile = "diaryDB.txt"

# Helper function to save the diary database to file


def saveDiary(diaryDB):
    with open(diaryFile, "w") as f:
        f.writelines(f"{timestamp}\n{entry}\n" for timestamp,
                     entry in diaryDB.items())


# Helper function to load the diary database from file


def loadDiaryFile():
    diaryDB = {}
    try:
        with open(diaryFile, "r") as f:
            lines = f.readlines()
            for i in range(0, len(lines), 2):
                timestamp = lines[i].strip()
                entry = lines[i+1].strip()
                diaryDB[timestamp] = entry
    except FileNotFoundError:
        pass
    return diaryDB

# Helper function to prompt for the password


def promptPassword():
    print("\033[32m=\033[0m" * 15)
    print("* DIARY LOGIN *")
    print("\033[35m=\033[0m" * 15)
    print()
    password = input("Enter your password: ")
    return password == passWord

# Helper function to add a diary entry


def addEntry(diaryDB):
    entry = input("Enter diary entry: ").capitalize()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    diaryDB[timestamp] = entry
    saveDiary(diaryDB)

# Helper function to view the diary entries


def viewEntries(diaryDB):
    timestamps = sorted(diaryDB.keys(), reverse=True)
    if len(timestamps) == 0:
        print("No entries to view.")
        input("Press enter to go back to the menu.")
        os.system('cls' if os.name == 'nt' else 'clear')
        return

    currentIndex = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(diaryDB[timestamps[currentIndex]])
        if currentIndex == len(timestamps) - 1:
            choice = input(
                "No more entries. Press enter to go back to the menu.")
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            choice = input(
                "Press enter for the next entry, or 'm' to go back to the menu.")
        if choice == "m":
            break
        else:
            currentIndex += 1
            os.system('cls' if os.name == 'nt' else 'clear')

# Helper function to view an entry from an exact date


def viewEntryDate(diaryDB):
    date = input("Enter date (YYYY-MM-DD): ")
    entryFound = False
    for timestamp, entry in diaryDB.items():
        if timestamp.startswith(date):
            print(entry)
            entryFound = True
    if not entryFound:
        print("No entries found for that date.")
    input("Press enter to go back to the menu.")
    os.system('cls' if os.name == 'nt' else 'clear')


# Main function to run the program


def main():
    # Load the diary database from file
    diaryDB = loadDiaryFile()

    # Prompt for the password
    if not promptPassword():
        print("\033[31mACCESS DENIED\033[0m")
        time.sleep(1)
        print()
        print(
            "Please try again later. If you forgot your password, please contact the administrator."
        )
        print()
        print("Thank you for using my diary program.")
        return
    print()
    print("\033[36mACCESS GRANTED\033[0m")
    time.sleep(2)
    # Main menu loop
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[35m=\033[0m" * 14)
        print("* DIARY MENU *")
        print("\033[32m=\033[0m" * 14)
        print("1. Add entry")
        print("2. View entries")
        print("3. View entry from date")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            addEntry(diaryDB)
        elif choice == "2":
            viewEntries(diaryDB)
        elif choice == "3":
            viewEntryDate(diaryDB)
        elif choice == "4":
            print("\033[31mExiting program.\033[0m")
            print()
            print("Thank you for using my diary program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
