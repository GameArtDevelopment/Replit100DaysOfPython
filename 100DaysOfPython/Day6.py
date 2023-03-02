print("\033[4m""****SECURE LOGIN****""\033[0m")
print()
name = input("What's you name? ")
print()
print("Hi " + name, ", let's create a username and password.")
print()
username = input("username: ")
print()
password = input("password: ")
print()
if username == "Steven" and password == "Rogers":
    print("\033[31m", "I can do this all day!", "\033[0m")
elif username == "Peter" and password == "Parker":
    print("\033[36m""With great power comes great responsibility!""\033[0m")
elif username == "Tony" and password == "Stark":
    print("\033[33m""I am Iron man!""\033[0m")
else:
    print("You entered the wrong information.")
print()
print("Thank you for trying my login program. I hope you enjoyed it.")
print("ANSWER: usernames are -> Steven, Peter, Tony and passwords are -> Rogers, Parker, Stark. Remember, capital letters matter.")
