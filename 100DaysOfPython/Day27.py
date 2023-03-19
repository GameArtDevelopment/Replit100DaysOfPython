import random
import os
import time
play = "yes"


def character1():
    print("Please enter your warrior name:")
    name = input()
    time.sleep(1)
    print(
        "Please enter your warrior type",
        "\033[32m(Soldier, Elf, Archer, Wizard, Lancer, Priest, Orc, Shadowknight)\033[0m",
        ":")
    charType = input()
    time.sleep(1)
    print("WARRIOR:", "\033[34m", name, "\033[0m", "TYPE:", "\033[34m", charType,
          "\033[0m")
    return name, charType


def char(max):
    roll = random.randint(1, max)
    return roll


def rollCharHealth():
    max6 = char(6)
    max8 = char(12)
    health = ((max6 * max8) / 2) + 10
    return health


def rollCharStrength():
    max6 = char(6)
    max8 = char(12)
    health = ((max6 * max8) / 2) + 12
    return health


while play == "yes":
    os.system("clear")
    print("\033[31m*** CHARACTER BUILDER ***\033[0m")
    character1()
    print("HEALTH:", "\033[34m", rollCharHealth(), "\033[0m")
    print("STRENGTH:", "\033[34m", rollCharStrength(), "\033[0m")
    print("May your name go down in legend...")
    play = input("Create another character? ")
print("Thank you for using my simple Character Builder program.")
print()
