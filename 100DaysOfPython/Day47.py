import os
characters = {}
print()

while True:
    os.system('clear')
    print("\033[34m============================\033[0m")
    print("* Welcome to my card game! *")
    print("\033[35m============================\033[0m")
    print()
    name = input("Enter character name or enter 'B' to battle: ").capitalize()
    if name == 'B':
        break

    stats = {}
    stats['Speed'] = int(input("Enter speed stat: "))
    stats['Strength'] = int(input("Enter strength stat: "))
    stats['Magic'] = int(input("Enter magic stat: "))
    stats['Health'] = int(input("Enter health stat: "))

    characters[name] = stats

player1Score = 0
player2Score = 0

while True:
    os.system('clear')
    print("\033[32m============================\033[0m")
    print("***      \033[31mBATTLE TIME\033[0m     ***")
    print("\033[33m============================\033[0m")
    print()
    print("Player 1, choose a card:")
    for card in characters.keys():
        print(card)
    print("Enter 'q' to quit the game.")
    player1Card = input().capitalize()

    if player1Card == 'Q':
        print("Game over. Player 1 quits.")
        break

    if player1Card not in characters:
        print("Invalid card.")
        continue

    print("Player 2, choose a card:")
    for card in characters.keys():
        print(card)
    print("Enter 'q' to quit the game.")
    player2Card = input().capitalize()

    if player2Card == 'Q':
        print("Game over. Player 2 quits.")
        break

    if player2Card not in characters:
        print("Invalid card.")
        continue
    os.system('clear')
    print("\033[32m============================\033[0m")
    print("***         \033[31mFIGHT\033[0m        ***")
    print("\033[33m============================\033[0m")
    print()
    print("Stats: Speed, Strength, Magic, Health")
    stat = (input("Choose a stat to compare: ")).capitalize()

    if stat not in characters[player1Card] or stat not in characters[player2Card]:
        print("Invalid stat.")
        continue

    player1StatValue = characters[player1Card][stat]
    player2StatValue = characters[player2Card][stat]

    print(f"{player1Card}'s {stat}: {player1StatValue}")
    print(f"{player2Card}'s {stat}: {player2StatValue}")

    if player1StatValue > player2StatValue:
        print(f"{player1Card} wins!")
        player1Score += 1
    elif player2StatValue > player1StatValue:
        print(f"{player2Card} wins!")
        player2Score += 1
    else:
        print("It's a tie!")

    print(f"Score: Player 1 - {player1Score}, Player 2 - {player2Score}\n")

    if player1Score == 3:
        print("\033[32mPlayer 1 wins!\033[0m")
        break
    elif player2Score == 3:
        print("\033[33mPlayer 2 wins!\033[0m")
        break

    input("Press enter to continue...")
    print()
print()
print("Thanks for playing!")
print()
print("Follow me on Twitter: https://twitter.com/EnjoyTh3Ride for more Python projects!")
print()
