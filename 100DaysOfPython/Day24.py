import random
print("\033[31m****  WELCOME TO INFINITY DICE   ****\033[0m")
print()

sides = int(input("How many sides?: "))
play = "yes"


def rollDice(sides):
    print("You rolled ", "\033[32m", random.randint(1, sides), "\033[0m")
    print()


while play == "yes":
    rollDice(sides)
    play = input("Do you want to roll again? ")

print()
print("Thank you for trying my roll a dice.")
print()
