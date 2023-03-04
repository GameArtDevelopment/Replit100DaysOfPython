import random
num = random.randint(1, 100)
attempts = 0
found = False

while not found:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess == num:
        found = True
        print()
        print("You guessed it in {} attempts!".format(attempts))
    elif guess < num:
        print()
        print("The number you are guessing is too low.")
    else:
        print()
        print("The number you are guessing is too high.")
print()
print("Thanks for playing!")
print()
print("Credit to NeuralNine https://www.youtube.com/watch?v=-FqZKqw-tvE")
print()
