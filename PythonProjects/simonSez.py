import random
import time
import os
numbers = "123456789"
simon = ""

for score in range(0, 10):
    simon += random.choice(numbers)
    for num in simon:
        print(num)
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
    guess = input("Guess the number: ")
    if guess != simon:
        break
print()
print("Game Over! Your score is " + str(score))
print()
print("Thanks for playing!")
print()
print("Credits: NeuralNine. https://www.youtube.com/watch?v=-FqZKqw-tvE")
print()
