def sortByScore(contents):
    return contents[1]


data_list = []

with open("high.score", "r") as f:
    for line in f:
        initials, score = line.strip().split(",")
        score = int(score)
        data_list.append((initials, score))

data_list.sort(key=sortByScore, reverse=True)
winner = data_list[0]
print("=" * 36)
print("\033[33m* Welcome to my High Score program *\033[0m")
print("=" * 36)
print()
print(
    f"The winner is \033[32m{winner[0]}\033[0m with a HIGH SCORE of \033[32m{winner[1]}\033[0m.")
print()
print("Thank you for using my High Score program")
print()
print(
    "Follow me on twitter: \033[34mhttps://twitter.com/EnjoyTh3Ride\033[0m for more projects like this one")
print()
