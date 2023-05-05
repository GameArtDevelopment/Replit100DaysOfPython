import random
import time
import os

opponetWins = ""
warriorWins = ""
rounds = 0
play = "yes"


def roll(max):
    roll = random.randint(1, max)
    return roll


def rollHealth():
    max6 = roll(6)
    max8 = roll(12)
    health = ((max6 * max8) / 2) + 10
    return health


def rollStrength():
    max6 = roll(6)
    max8 = roll(12)
    strength = ((max6 * max8) / 2) + 12
    return strength

print("="*30)
print("\033[31m *** WARRIOR BATTLE ARENA ***\033[0m")
print("="*30)
print()
time.sleep(1)
print("Please enter your warrior name:")
warrior = input()
print("Please enter your warrior type (Soldier, Elf, Archer, Wizard, Lancer, Priest, Orc, Shadowknight):")
warriorType = input()
print()
warriorHealth = rollHealth()
warriorStrength = rollStrength()
print("HEALTH:", "\033[34m", warriorHealth, "\033[0m")
print("STRENGTH:", "\033[34m", warriorStrength, "\033[0m")
print("May your name go down in Legend...")
print()
print("WARRIOR:", "\033[34m", warrior, "\033[0m", "TYPE:", "\033[34m", warriorType,
      "\033[0m")
time.sleep(3)
print("Please enter your opponent's name:")
oppName = input()
print("Please enter your opponent's rollacter type (Soldier, Elf, Archer, Wizard, Lancer, Priest, Orc, Shadowknight):")
oppType = input()
opponentHealth = rollHealth()
opponentStrength = rollStrength()
print("HEALTH:", "\033[34m", opponentHealth, "\033[0m")
print("STRENGTH:", "\033[34m", opponentStrength, "\033[0m")
print("May opponent,", oppName, "go down in Legend...")
print()
print("OPPONENT:", "\033[34m", oppName, "\033[0m", "TYPE:", "\033[34m", oppType,
      "\033[0m")
time.sleep(4)
print()
while warriorHealth > 0 and opponentHealth > 0:
    os.system("clear")
    print("Let the Round Begin...")
    time.sleep(1)
    print("\033[31m*** BATTLE ARENA ***\033[0m")
    print("WARRIOR:", "\033[34m", warrior, "\033[0m", "TYPE:", "\033[34m", warriorType,
          "\033[0m")
    print("HEALTH:", "\033[34m", warriorHealth, "\033[0m")
    print("STRENGTH:", "\033[34m", warriorStrength, "\033[0m")
    print()
    print("OPPONENT:", "\033[34m", oppName, "\033[0m", "TYPE:", "\033[34m", oppType,
          "\033[0m")
    print("HEALTH:", "\033[34m", opponentHealth, "\033[0m")
    print("STRENGTH:", "\033[34m", opponentStrength, "\033[0m")
    print()
    warriorRoll = roll(6)
    opponentRoll = roll(6)
    hit = abs(warriorStrength - opponentStrength) + 1
    if warriorRoll > opponentRoll:
        warriorHealth = warriorHealth - hit
        print("You hit your opponent!")
        print("Your opponent's health is now", opponentHealth)
        time.sleep(2)
    elif warriorRoll < opponentRoll:
        opponentHealth = opponentHealth - hit
        print("You got hit!")
        print("Your health is now", warriorHealth)
        time.sleep(2)
    else:
        print("You both missed!")
        time.sleep(2)

    if warriorHealth <= 0:
        print("You have died!")
        print("Your opponent is the winner!")
        winner = oppName
        time.sleep(2)
        break
    elif opponentHealth <= 0:
        print("Your opponent has died!")
        print("You are the winner!")
        winner = warrior
        time.sleep(2)
        break
    else:
        print("The battle continues...")
        rounds += 1
        time.sleep(2)
        print()
print(winner, "is the winner!, in", rounds, "rounds!")
print()
print("Thank you for playing!")
print()
print("Please play again soon!")
print()
