import random
print("\033[31m*****  CHARACTER STAT GENERATOR  *****\033[0m")
print()


sides = int(input("How many sides do you want your dice to have?: "))
play = "yes"


def rollDice(sides):
    roll = random.randint(1, sides)
    return roll


def rollAnotherDice():
    roll6 = rollDice(6)
    roll8 = rollDice(8)
    health = roll6 * roll8

    print()
    return health


while play == "yes":
    print()
    player = input("Name your Soldier: ")
    print()
    rollDice(sides)
    health = str(rollAnotherDice())
    print(player+"\033[32m", " your health is ",
          "\033[0m", "\033[33m", health, "HP", "\033[0m")
    print()
    play = input("Do you want to name another soldier? ")

print()
print("Thank you for trying my Character Stat Generator.")
print()
