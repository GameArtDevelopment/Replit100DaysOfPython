from getpass import getpass as input
print("\033[31m", "****Welcome to ROCK, PAPER, SCISSORS. version 1.1****",
      "\033[0m")
print("A two-player game, and whoever wins three battles will decide who is the actual rock, paper, scissors champion. So let's start with player names.")
print()
playerName1 = input("What is your name player 1? ")
print()
playerName2 = input("What is your name player 2? ")
print()
print("Hi", playerName1, ",and", playerName2,
      ", let's get ready to play... ROCK, PAPER, SCISSORS!")
rock = "r" and "🪨"
paper = "p" and "📄"
scissors = "s" and "✂️"
counter1 = 0
counter2 = 0
print("\033[31m", "***INSTRUCTIONS***", "\033[0m")
print()
print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. You must enter one of these letters",
      "\033[35m", 'r, p, s', "\033[0m", "and press", "\033[34m", "ENTER/RETURN", "\033[0m", "-> R = rock, P = paper, S = scissors. Python's getpass will hide your entry.")
print("")
print()
while True:
    if counter1 == 3:
        print(playerName1, "won", counter1,
              "games, and is the Rock Paper Scissors CHAMPION!")
        break
    if counter2 == 3:
        print(playerName2, "won", counter2,
              "games, and is the Rock Paper Scissors CHAMPION!")
        break
    player1 = input("Enter your weapon of choice ").lower()
    print()
    player2 = input("Enter your weapon of choice ").lower()
    print()
    if (player1 == "r" and player2 == "s"):
        print(playerName1, "wins with 🪨")
        counter1 += 1
        print()
        continue
    elif (player1 == "r" and player2 == "p"):
        print(playerName2, "wins with 📄")
        counter2 += 1
        print()
        continue
    elif (player1 == "r" and player2 == "r"):
        print("Draw")
        print()
        continue
    elif (player1 == "p" and player2 == "r"):
        print(playerName1, "wins with 📄")
        counter1 += 1
        print()
        continue
    elif (player1 == "p" and player2 == "s"):
        print(playerName2, "wins with ✂️")
        counter2 += 1
        print()
        continue
    elif (player1 == "p" and player2 == "p"):
        print("Draw")
        print()
        continue
    elif (player1 == "s" and player2 == "p"):
        print(playerName1, "wins with ✂️")
        counter1 += 1
        print()
        continue
    elif (player1 == "s" and player2 == "r"):
        print(playerName2, "wins with 🪨")
        counter2 += 1
        print()
        continue
    elif (player1 == "s" and player2 == "s"):
        print("Draw")
        print()
        continue
    else:
        print("Game Over. Someone needed to enter the correct letter. Please try again.")
print()
print("Thank you for playing. I hope you enjoyed it!")
print()
