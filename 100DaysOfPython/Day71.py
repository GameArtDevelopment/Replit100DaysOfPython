import hashlib
import secrets
import os.path

# welcome message
print("\033[32m=\033[0m" * 35)
print("* WELCOME TO THE PASSWORD MANAGER *")
print("\033[33m=\033[0m" * 35)


def add_user():
    # Prompt user for username and password
    os.system("clear")
    while True:
        username = input("Enter a username: ")
        # Check if the username already exists in the database
        with open("db.txt", "r") as f:
            for line in f:
                fields = line.strip().split(",")
                if fields[0] == username:
                    print(
                        "Username already exists. Please choose a different username.")
                    break
            else:
                break
    password = input("Enter a password: ")
    # Generate a random 4-digit salt
    salt = secrets.randbelow(10000)
    # Append the salt to the password and hash it using sha256
    salted_password = password + str(salt)
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    # Save the username, salt, and hashed password to a file
    with open("db.txt", "a") as f:
        f.write(username + "," + str(salt) + "," + hashed_password + "\n")

    print("User created successfully!")


def login():
    # Prompt user for username and password
    os.system("clear")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the user exists in the database
    with open("db.txt", "r") as f:
        for line in f:
            fields = line.strip().split(",")
            if fields[0] == username:
                salt = int(fields[1])
                hashed_password = fields[2]
                break
        else:
            print()
            print("\033[31mInvalid username or password.\033[0m")
            print()
            return

    # Hash the input password with the stored salt and compare to stored hash
    salted_password = password + str(salt)
    if hashlib.sha256(salted_password.encode()).hexdigest() == hashed_password:
        print()
        print("\033[32mLogin successful!\033[0m")
        print()
        print("Welcome back, " + username + "!")
        print("="*20)
    else:
        print()
        print("\033[31mInvalid username or password.\033[0m")
        print()


# Check if the database file exists, create it if it doesn't
if not os.path.isfile("db.txt"):
    open("db.txt", "w").close()

# Main program loop
while True:
    print("1. Add user")
    print("2. Login")
    print("3. \033[31mExit\033[0m")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        login()
    elif choice == "3":
        print()
        print("\033[31mExiting program.\033[0m")
        break
    else:
        print("Invalid choice. Please try again.")
print()
print("\033[32m=\033[0m" * 43)
print("* THANK YOU FOR USING MY PASSWORD MANAGER *")
print("\033[33m=\033[0m" * 43)
