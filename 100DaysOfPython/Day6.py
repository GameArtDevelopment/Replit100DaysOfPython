print("\033[31m****** SECURE LOGIN ******\033[0m")
print()
name = input("Enter your name: ")
print()
print("Hello, " + name + "!")
print()
print("Please enter your username and password to continue.")
print()
username = input("Username: ")
print()
password = input("Password: ")
print()
if username == "Steven" and password == "Rogers":
    print("\033[31mAccess Granted, You can do this all day!\033[0m")
elif username == "Peter" and password == "Parker":
    print(
        "\033[36mAccess Granted, With great power comes great responsibility!\033[0m")
elif username == "Tony" and password == "Stark":
    print("\033[33mAccess Granted! You are Iron Man!\033[0m")
else:
    print("-------------------------------------------------")
    print("\033[31mAccess Denied, You are not worthy!\033[0m")

print()
print("Thank you for using the Secure Login System, " + name + "!")
print()
print("ANSWER: usernames are -> ", "\033[32m", "Steven, Peter, Tony", "\033[0m", "and asswords are -> ",
      "\033[34m", "Rogers, Parker, Stark.", "\033[0m", "Remember, capital letters matter.")
print()
