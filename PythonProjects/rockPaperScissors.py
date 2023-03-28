import random
print("****Rock Paper Scissors****")
print()
print("let's play Rock Paper Scissors")
print()
userWins = 0
compWins = 0

options = ["rock", "paper", "scissors"]

while True:
    print()
    userInput = input("Choose rock, paper, scissors or Q(Quit): ").lower()
    print()
    if userInput == "q":
        break

    if userInput not in options:
        continue

    randomNumber = random.randint(0, 2)  # rock 0, paper 1, scissors 2
    compPick = options[randomNumber]
    print(f"Computer chose {compPick}")
    print()

    if userInput == "rock" and compPick == "scissors":
        print(f"You Won!")
        userWins += 1

    elif userInput == "paper" and compPick == "rock":
        print(f"You Won!")
        userWins += 1

    elif userInput == "scissors" and compPick == "paper":
        print(f"You Won!")
        userWins += 1
    elif userInput == "rock" and compPick == "rock":
        print(f"Tie!")
        userWins += 0
    elif userInput == "paper" and compPick == "paper":
        print(f"Tie!")
        userWins += 0
    elif userInput == "scissors" and compPick == "scissors":
        print(f"Tie!")
        userWins += 0

    else:
        print("You Lost!")
        compWins += 1

print(f"User Wins: {userWins}")
print()
print(f"Computer Wins: {compWins}")
print()
print(f"Total victories: {userWins + compWins}")
print()
print("Thanks for playing!")
print()
print("Part of the 5 mini projects from YouTube sensation -> Tech With Tim")
