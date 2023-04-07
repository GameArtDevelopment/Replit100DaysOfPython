import random
import os
import time

bingo = []


def generate_random_number():
    number = random.randint(1, 90)
    return number


def pretty_print_bingo():
    print("\033[34m======================\033[0m")
    print("======= BINGO ========")
    print("\033[34m======================\033[0m")
    print()
    for row in bingo:
        print(row)
    time.sleep(2)


while True:
    os.system("clear")
    numbers = []
    for i in range(8):
        numbers.append(generate_random_number())

    numbers.sort()

    bingo = [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BINGO", numbers[4]],
        [numbers[5], numbers[6], numbers[7]]
    ]

    pretty_print_bingo()
    print()
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == 'n':
        print()
        print("Thank you playing my random Bingo card.")
        break
