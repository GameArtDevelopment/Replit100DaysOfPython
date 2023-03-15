print("\033[31m*******     WELCOME     *******\033[0m")
print()
print("Let's verify you.")
print()
username = "josh"
password = "pass"


def login():
    while True:
        user = input("Please enter your username: ").lower()
        print()
        pass1 = input("Please enter your password: ").lower()
        print()
        if user == username and pass1 == password:
            print("Welcome, Joseph")
            break
            print()
        else:
            print(
                "Whoops! I don't recognize that username or password. Please Try Again.")
            continue
            print()


login()
print()
print("Thank you for trying my subroutine challenge.")
print()
