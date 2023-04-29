import random
import os
import time


def generationGenerator():
    print("================================")
    print("\033[1m**     GENERATION GENERATOR   **\033[0m")
    print("================================")
    print()
    name = input("What is your name?. ")
    print()
    print(f"Hi \033[1m{name}\033[0m")
    print()
    print(
        f"Hi \033[1m{name}\033[0m, I'm  a generation generator. I will tell you what generation you belong to.")
    print()
    year = int(input("What year were you born?. "))
    print()
    if (year <= 1945 and year >= 1925):
        print("You belong to the \033[1;31mTraditionalist Generation\033[0m.")
        print()
        print(
            f"Thank you \033[1m{name}\033[0m for trying my generation generator.")
        print()
    elif (year <= 1964 and year >= 1946):
        print("You belong to the \033[1;32mBaby Boomer Generation\033[0m.")
        print()
        print(
            f"Thank you \033[1m{name}\033[0m for trying my generation generator.")
        print()
    elif (year <= 1980 and year >= 1965):
        print("You belong to the \033[1;33mGeneration X Generation\033[0m.")
        print()
        print(
            f"Thank you \033[1m{name}\033[0m for trying my generation generator.")
        print()
    elif (year <= 1996 and year >= 1981):
        print("You belong to the \033[1;34mMillennial Generation\033[0m.")
        print()
        print(
            f"Thank you \033[1m{name}\033[0m for trying my generation generator.")
        print()
    elif (year <= 2012 and year >= 1997):
        print("You belong to the \033[1;35mGeneration Z Generation\033[0m.")
        print()
        print(
            f"Thank you \033[1m{name}\033[0m for trying my generation generator.")
        print()
    elif (year <= 2020 and year >= 2013):
        print(
            "You belong to the \033[1;36mGeneration Alpha Generation\033[0m.")
        print()
        print(
            f"Thank you \033[1m{name}\033[0m for trying my generation generator.")
        print()
    else:
        print("You are not part of any generation.")
        print()
        print(
            f"Thank you \033[1m{name}\033[0m for trying my generation generator.")
        print()
    print("================================")
    print("\033[1m**     GENERATION GENERATOR   **\033[0m")
    print("================================")
    print()
    print("Generation information provided by www.generationresearch.com.")
    print()
    time.sleep(3)


def numGuess():
    print("================================")
    print("**     GUESS THE NUMBER       **")
    print("================================")
    print()
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    print()

    play_again = True

    while play_again:
        number = random.randint(1, 100)
        numberGuess = 0
        counter = 0

        while True:
            if numberGuess == number:
                print()
                counter += 1
                print("\033[34m", "You Got It!, it only took you",
                      "\033[0m", "\033[31m", counter, "\033[0m", "\033[34m", "attempts", "\033[0m")
                print()
                time.sleep(1.5)
                break

            numberGuess = int(input("What is your guess? "))

            if numberGuess < number and numberGuess >= 0:
                print("Higher")
                counter += 1
                print()

            elif numberGuess > number and numberGuess <= 100:
                print("Lower")
                counter += 1
                print()

            elif numberGuess < 0:
                exit("You need to stay positive.")
                print()

            elif numberGuess > 100:
                print("Not sure why you entered that. Please try again.")
                counter += 1
                print()

        play_again_input = input("Would you like to play again? (Y/N) ")

        if play_again_input.lower() == "y":
            play_again = True
        else:
            play_again = False

    print("Great Job! Thank you for playing GUESS THE NUMBER game.")
    print()
    print("================================")
    print("**     GUESS THE NUMBER       **")
    print("================================")
    print()


def interestCalc():
    print("================================")
    print("**     INTEREST CALCULATOR    **")
    print("================================")
    print()
    print("A Python code calculates how much APR will cost.")
    print()

    while True:
        borrowed = int(input("How much money do you want to borrow? "))
        print()

        years = int(input("How many years will you borrow it for? "))
        print()

        apr = float(
            input("What is the annual interest rate (APR)? (e.g. 0.05 for 5%): "))
        print()

        for i in range(years):
            borrowed = borrowed * (1 + apr)
            print("On year", i+1, "you will owe: $",
                  "\033[32m", round(borrowed, 2), "\033[0m")

        print()
        print("Your total debt after borrowing $", borrowed, "at", round(apr*100, 2), "% APR for",
              years, "years is: $", "\033[32m", round(borrowed, 2), "\033[0m")
        print()

        choice = input(
            "Press Enter to enter another amount or type \033[31m'exit'\033[0m to quit: ")
        if choice.lower() == "exit":
            break

    print()
    print("Thank you for trying my INTEREST CALCULATOR.")
    print()
    print("================================")
    print("**     INTEREST CALCULATOR    **")
    print("================================")
    print()


def diceRoll():
    print("================================")
    print("**     DICE ROLLER            **")
    print("================================")
    print()
    print("A Python code that rolls a dice.")
    print()
    import random
    sides = int(input("How many sides do you want your dice to have?: "))
    play = "yes"

    def rollDice(sides):
        roll = random.randint(1, sides)
        return roll

    while play == "yes":
        print()
        rollDice(sides)
        print("You rolled a ", "\033[32m", rollDice(sides), "\033[0m")
        print()
        play = input("Do you want to roll again? ")
    print()
    print("Thank you for trying my DICE ROLLER.")
    print()
    print("================================")
    print("**     DICE ROLLER            **")
    print("================================")
    print()


def toDoList():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;34m================================\033[0m")
    print("\033[1;34m**     TO DO LIST             **\033[0m")
    print("\033[1;34m================================\033[0m")
    print()
    print("A Python code that creates a to do list.")
    print()

    toDoList = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print("To Do List: ", toDoList)
        print()
        toDo = input("What do you want to add to your to do list? ")
        print()
        toDoList.append(toDo)

        exit_choice = input("Do you want to add more items? (y/n) ")
        if exit_choice.lower() == "n":
            break

    print("\n\033[1;32mThank you for using my TO DO LIST.\033[0m")
    print()
    input("Press enter to continue...")
    print()
    print("\033[32mThank you for trying my TO DO LIST.\033[0m")
    print()
    print("\033[96m================================\033[0m")
    print("\033[32m**     TO DO LIST             **\033[0m")
    print("\033[96m================================\033[0m")
    print()
