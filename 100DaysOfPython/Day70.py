import csv
import os
# create a title for the program
print("\033[35m=\033[0m"*30)
print("* Welcome to the secret club *")
print("\033[36m=\033[0m"*30)
print()
print("Please enter your username and password to continue.")


# Ask the user for their username and password
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")


# Open the CSV file
with open('100DaysOfPython/secret.csv', mode='r') as csv_file:
    # Create a dictionary reader
    csv_reader = csv.DictReader(csv_file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Store the username and password in variables
        username = row['username']
        password = row['password']

        # Check if the username and password match the user's input
        if input_username == username and input_password == password:
            # User is authenticated, do something here
            os.system('clear')
            print()
            print("Hello", username)
            break
    else:
        # User is not authenticated, handle error here
        os.system('clear')
        print()
        print("\033[31mInvalid username or password\033[0m")
        print("Try admin, admin_password or normal, normal_password")
        print()
print()
print("\033[36m=\033[0m"*35)
print("* Thank you for using my program *")
print("\033[35m=\033[0m"*35)
print()
