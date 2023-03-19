import random
import time
import os

# Character Builder


def characterBuilder():
    print("Welcome to the Character Builder!")
    time.sleep(1)
    print("Please enter your name:")
    name = input()
    print("Please enter your character type (Human, Elf, Wizard, Orc):")
    charType = input()
    print("Please enter your health:")
    health = int(input())
    print("Please enter your strength:")
    strength = int(input())
    print("May your name go down in Legend...")
    time.sleep(5)
    return name, charType, health, strength

# Character Stats


def characterStats(name, charType, health, strength):
    print(f"Name: {name}")
    print(f"Character Type: {charType}")
    print(f"Health: {health}")
    print(f"Strength: {strength}")

# Character Battle


def characterBattle(name, charType, health, strength):
    print(f"Welcome to the Battle Arena, {name}!")
    time.sleep(4)
    print("Please enter your opponent's name:")
    opponentName = input()
    print("Please enter your opponent's character type (Human, Elf, Wiard, Orc):")
    opponentCharType = input()
    print("Please enter your opponent's health:")
    opponentHealth = int(input())
    print("Please enter your opponent's strength:")
    opponentStrength = int(input())
    print("May your name go down in Legend...")
    time.sleep(4)
    return opponentName, opponentCharType, opponentHealth, opponentStrength

# Battle Stats


def battleStats(name, charType, health, strength, opponentName, opponentCharType, opponentHealth, opponentStrength):
    print(f"{name} vs. {opponentName}")
    print(f"{name}'s Health: {health}")
    print(f"{name}'s Strength: {strength}")
    print(f"{opponentName}'s Health: {opponentHealth}")
    print(f"{opponentName}'s Strength: {opponentStrength}")

# Battle


def battle(name, charType, health, strength, opponentName, opponentCharType, opponentHealth, opponentStrength):
    while health > 0 and opponentHealth > 0:
        print(f"{name}'s turn!")
        time.sleep(5)
        print(f"{name} attacks {opponentName}!")
        time.sleep(5)
        opponentHealth -= strength
        print(f"{opponentName}'s Health: {opponentHealth}")
        time.sleep(5)
        if opponentHealth <= 0:
            print(f"{name} wins!")
            break
        print(f"{opponentName}'s turn!")
        time.sleep(5)
        print(f"{opponentName} attacks {name}!")
        time.sleep(5)
        health -= opponentStrength
        print(f"{name}'s Health: {health}")
        time.sleep(5)
        if health <= 0:
            print(f"{opponentName} wins!")
            break

# Main Menu


def mainMenu():
    print("Welcome to the Main Menu!")
    time.sleep(2)
    print("Press 1 to open the Character Builder")
    time.sleep(2)
    print("Press 2 to open the Battle Arena")
    time.sleep(2)
    print("Press 3 to exit the program")
    time.sleep(2)
    print("Press any other number to open the Main Menu")
    userInput = int(input())
    return userInput


# Main
while True:
    os.system("clear")
    print("\033[34mCHARACTER BATTLE BUILDER\033[0m")
    time.sleep(2)
    userInput = mainMenu()
    if userInput == 1:
        name, charType, health, strength = characterBuilder()
        characterStats(name, charType, health, strength)
        time.sleep(2)
    elif userInput == 2:
        opponentName, opponentCharType, opponentHealth, opponentStrength = characterBattle(
            name, charType, health, strength)
        battleStats(name, charType, health, strength, opponentName,
                    opponentCharType, opponentHealth, opponentStrength)
        time.sleep(2)
        battle(name, charType, health, strength, opponentName,
               opponentCharType, opponentHealth, opponentStrength)
    elif userInput == 3:
        print("Exiting Program...")
        exit()
    else:
        continue

print("Thank you for playing!")

# Name Your Legend:
# Sheila the Almighty


# Character Type (Human, Elf, Wiard, Orc):
# Human

# Sheila the Almighty
# HEALTH: 40
# STRENGTH: 26

# May your name go down in Legend...
