import os
from datetime import datetime
import hashlib
import binascii

# Define the diary database filename
diaryFile = "diaryV2DB.txt"
saltFile = "salt.txt"
hashFile = "hash.txt"

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

# Helper function to save salt to file


def saveSalt(salt):
    with open(saltFile, "w") as f:
        f.write(salt)

# Helper function to load salt from file


def loadSalt():
    try:
        with open(saltFile, "r") as f:
            salt = f.read().strip()
    except FileNotFoundError:
        salt = None
    return salt

# Helper function to save hash to file


def saveHash(hash):
    with open(hashFile, "w") as f:
        f.write(hash)

# Helper function to load hash from file


def loadHash():
    try:
        with open(hashFile, "r") as f:
            hash = f.read().strip()
    except FileNotFoundError:
        hash = None
    return hash

# Helper function to prompt for the username and password


def promptUsernamePassword():
    print("\033[32m=\033[0m" * 15)
    print("* DIARY LOGIN *")
    print("\033[35m=\033[0m" * 15)
    print()
    while True:
        username = input("Create a username: ")
        if username.strip() == "":
            print("Username cannot be empty. Please try again.")
        else:
            break
    while True:
        password = input("Create a password: ")
        if password.strip() == "":
            print("Password cannot be empty. Please try again.")
        else:
            break
    return username, password

# Helper function to hash and salt the password


def hashPassword(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
        saveSalt(binascii.hexlify(salt).decode())
    else:
        salt = binascii.unhexlify(salt.encode())
    hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    saveHash(binascii.hexlify(hash).decode())
    return salt, hash

# Helper function to check the username and password


def checkUsernamePassword():
    salt = loadSalt()
    hash = loadHash()
    if salt is None or hash is None:
        username, password = promptUsernamePassword()
        salt, hash = hashPassword(password, salt)
        saveDiary({})
    else:
        password = input("Enter your password: ")
        hashToCheck = hashlib.pbkdf2_hmac(
            'sha256', password.encode(), binascii.unhexlify(salt.encode()), 100000)
        if hash == binascii.hexlify(hashToCheck).decode():
            username = input("Enter your username: ")
        else:
            print("Incorrect password.")
            username, password = promptUsernamePassword()
            salt, hash = hashPassword(password, salt)
            saveDiary({})
    return username, password

# Helper function to add a diary entry


def addEntry(diaryDB):
    entry = input("Enter diary entry: ").capitalize()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    diaryDB[timestamp] = entry
    saveDiary(diaryDB)

# Helper function to view the diary entries


def viewEntries(diaryDB):
    timestamps = sorted(diaryDB.keys(), reverse=True)
    for timestamp in timestamps:
        print(f"{timestamp} - {diaryDB[timestamp]}")

# Helper function to delete a diary entry


def deleteEntry(diaryDB):
    timestamps = sorted(diaryDB.keys(), reverse=True)
    for i, timestamp in enumerate(timestamps):
        print(f"{i+1}. {timestamp} - {diaryDB[timestamp]}")
    while True:
        try:
            option = int(input("Enter the entry number to delete: "))
            if option < 1 or option > len(timestamps):
                print("Invalid option. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid option. Please try again.")
    del diaryDB[timestamps[option-1]]
    saveDiary(diaryDB)

# Helper function to edit a diary entry


def editEntry(diaryDB):
    timestamps = sorted(diaryDB.keys(), reverse=True)
    for i, timestamp in enumerate(timestamps):
        print(f"{i+1}. {timestamp} - {diaryDB[timestamp]}")
    while True:
        try:
            option = int(input("Enter the entry number to edit: "))
            if option < 1 or option > len(timestamps):
                print("Invalid option. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid option. Please try again.")
    entry = input("Enter diary entry: ").capitalize()
    timestamp = timestamps[option-1]
    diaryDB[timestamp] = entry
    saveDiary(diaryDB)

# Helper function to search for a diary entry


def searchEntry(diaryDB):
    search = input("Enter search term: ").lower()
    for timestamp, entry in diaryDB.items():
        if search in entry.lower():
            print(f"{timestamp} - {entry}")

# Helper function to display the menu


def displayMenu():
    print("\033[32m=\033[0m" * 15)
    print("* DIARY MENU *")
    print("\033[35m=\033[0m" * 15)
    print("1. Add diary entry")
    print("2. View diary entries")
    print("3. Delete diary entry")
    print("4. Edit diary entry")
    print("5. Search diary entries")
    print("6. Exit")
    print()

# Helper function to prompt for the menu option


def promptMenuOption():
    while True:
        try:
            option = int(input("Enter option: "))
            if option < 1 or option > 6:
                print("Invalid option. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid option. Please try again.")
    return option


# Main function
def main():
    diaryDB = loadDiaryFile()
    username, password = checkUsernamePassword()
    print(f"Welcome, {username}!")
    while True:
        displayMenu()
        option = promptMenuOption()
        if option == 1:
            addEntry(diaryDB)
        elif option == 2:
            viewEntries(diaryDB)
        elif option == 3:
            deleteEntry(diaryDB)
        elif option == 4:
            editEntry(diaryDB)
        elif option == 5:
            searchEntry(diaryDB)
        elif option == 6:
            print("Thank you for using my diary. Goodbye!")
            print()
            break
        print()


if __name__ == "__main__":
    main()
