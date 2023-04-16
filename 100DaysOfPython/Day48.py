import os


def sortByScore(item):
    return item[1]


data_list = []

while True:
    os.system("clear")
    print("=" * 36)
    print("\033[32m* Welcome to my High Score program *\033[0m")
    print("=" * 36)
    print()
    initials = input("Please enter your initials: ").upper()
    score = int(input("Please enter your score: "))

    with open("high.score", "a") as file:
        file.write(f"{initials},{score}\n")

    data_list.append((initials, score))

    if input("Do you want to enter more data? (y/n): ").lower() != "y":
        break

os.system("clear")
print("=" * 38)
print("\033[33m*    List of your High Scores    *\033[0m")
print("=" * 38)
print("\033[33mInitials  |   Score\033[0m")
print("-" * 25)

data_list.sort(key=sortByScore, reverse=True)

for initials, score in data_list:
    print(f"{initials:<10}\t{score:>5}")

print("\nThank you for using my High Score program\n")
print(
    "Follow me on twitter: \033[34mhttps://twitter.com/EnjoyTh3Ride\033[0m for more projects like this one\n")
