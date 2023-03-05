from getpass import getpass as input
print("\033[30m", "****Welcome to ROCK, PAPER, SCISSORS****", "\033[0m")
print("This is a 2 player game and only one battle will decide who is the true rock, paper, scissors champion. Let's start with player names.")
playerName1 = input("What is your name player 1? ")
playerName2 = input("What is your name player 2? ")
print("Hi", playerName1, ",and", playerName2,
      ", let's get ready to play... ROCK, PAPER, SCISSORS!")
rock = "r" and "🪨"
paper = "p" and "📄"
scissors = "s" and "✂️"
print("\033[31m", "***INSTRUCTIONS***", "\033[0m")
print()
print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock. You must enter one of these letters",
      "\033[35m", 'r, p, s and press ENTER/RETURN', "\033[0m", "-> R = rock, P = paper, S = scissors. Python's getpass will hide your entry from the other player.")
print("")
print()
player1 = input("Enter your weapon of choice ").lower()
print()
player2 = input("Enter your weapon of choice ").lower()
print()
if (player1 == "r" and player2 == "s"):
    print(playerName1, "wins with 🪨")
elif (player1 == "r" and player2 == "p"):
    print(playerName2, "wins with 📄")
elif (player1 == "r" and player2 == "r"):
    print("Draw")
elif (player1 == "p" and player2 == "r"):
    print(playerName1, "wins with 📄")
elif (player1 == "p" and player2 == "s"):
    print(playerName2, "wins with ✂️")
elif (player1 == "p" and player2 == "p"):
    print("Draw")
elif (player1 == "s" and player2 == "p"):
    print(playerName1, "wins with ✂️")
elif (player1 == "s" and player2 == "r"):
    print(playerName2, "wins with 🪨")
elif (player1 == "s" and player2 == "s"):
    print("Draw")
else:
    print("Game Over. Someone needed to enter the correct letter. Please try again.")
print()
print("Thank you for playing. Sorry, the game is not longer than one attempt. I have yet to learn how loops work.")
print()
