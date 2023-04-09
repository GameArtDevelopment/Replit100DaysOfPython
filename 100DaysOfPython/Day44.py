import random
import os
import time
bingo = []


def randomNumber():
    return random.randint(1, 90)


def bingoCard():
    numbers = []
    for i in range(8):
        num = randomNumber()
        while num in numbers:
            num = randomNumber()
        numbers.append(num)
    numbers.sort()
    return [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BG", numbers[4]],
        [numbers[5], numbers[6], numbers[7]]
    ]


def generateBingoCard():
    for row in bingo:
        print("\t|\t".join([str(item) for item in row]))


def playBingo():
    global bingo
    bingo = bingoCard()
    while True:
        print("\33[34m=====================\33[0m")
        print("*     BINGO CARD    *")
        print("\33[34m=====================\33[0m")
        print()
        generateBingoCard()
        print()
        num = int(input("Next Number: "))
        for row in range(3):
            for col in range(3):
                if bingo[row][col] == num:
                    bingo[row][col] = "\33[31mX\33[0m"
        slot = sum(row.count("\33[31mX\33[0m") for row in bingo)

        if slot == 8:
            time.sleep(1)
            print()
            print("Thank you for playing my BINGO game!")
            break
        time.sleep(1)
        os.system("clear")


playBingo()
