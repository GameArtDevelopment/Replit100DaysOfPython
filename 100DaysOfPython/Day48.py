import os
data_list = []

while True:
    os.system("clear")
    print("====================================")
    print("\033[32m* Welcome to my High Score program *\033[0m")
    print("====================================")
    print()
    initials = input("Please enter your initials: ").title()
    score = input("Please enter your score: ")

    score = int(score)

    with open("high.score", "a") as file:
        file.write(f"{initials} {score}\n")

    data_list.append((initials, score))

    choice = input("Do you want to enter more data? (y/n): ")
    if choice.lower() == "n":
        break

os.system("clear")
print("\033[32m=================================\033[0m")
print("\033[33m*    List of your High Score    *\033[0m")
print("\033[35m=================================\033[0m")
print()
print("\033[33mInitials  |   Score\033[0m")
for initials, score in data_list:
    print(f"{initials}        \t{score}")
print()
print("Thank you for using my High Score program")
print()
print(
    "Follow me on twitter: \033[34mhttps://twitter.com/EnjoyTh3Ride\033[0m for more projects like this one")
print()
