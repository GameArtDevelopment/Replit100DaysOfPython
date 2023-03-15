import random
print("\033[31m", "    ****GUESS A RANDOM NUMBER****", "\033[0m")
print()
number = random.randint(1, 1000)
numberGuess = 0
counter = 0
print("Guess a number between 1 - 1,000")
print()
while True:
    if numberGuess == number:
        print()
        counter += 1
        print("\033[34m", "You Got It!, it only took you", "\033[0m",
              "\033[31m", counter, "\033[0m", "\033[34m", "attempts",
              "\033[0m")
        print()
        break
    numberGuess = int(input("What is your guess? "))
    if numberGuess < number and numberGuess >= 0:
        print("Higher")
        counter += 1
        print()
        continue
    elif numberGuess > number and numberGuess <= 1000:
        print("Lower")
        counter += 1
        print()
        continue
    elif numberGuess < 0:
        exit("You need to stay positive.")
        print()
    elif numberGuess > 1000:
        print("Not sure why you entered that. Please try again.")
        counter += 1
        print()
print("Great Job! Thank you for playing GUESS THE RANDOM NUMBER game.")
print()
