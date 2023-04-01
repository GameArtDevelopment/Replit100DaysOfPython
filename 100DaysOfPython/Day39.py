import random
import os
import time

wordList = ["python", "strings", "variables", "random", "import",
            "repl", "decorators", "libraries", "loops", "booleans"]

word = random.choice(wordList)

attempts = 0
maxAttempts = 6
guessedLetters = []


def hangmanDisplay(attempts):
    if attempts == 0:
        print("________")
        print("|     |    ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|__________")
    elif attempts == 1:
        print("________")
        print("|     |    ")
        print("|     O    ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|__________")
    elif attempts == 2:
        print("________")
        print("|     |    ")
        print("|     O    ")
        print("|     |    ")
        print("|          ")
        print("|          ")
        print("|__________")
    elif attempts == 3:
        print("________")
        print("|     |    ")
        print("|     O    ")
        print("|    /|    ")
        print("|          ")
        print("|          ")
        print("|__________")
    elif attempts == 4:
        print("________")
        print("|     |    ")
        print("|     O    ")
        print("|    /|\   ")
        print("|          ")
        print("|          ")
        print("|__________")
    elif attempts == 5:
        print("________")
        print("|     |    ")
        print("|     O    ")
        print("|    /|\   ")
        print("|    /     ")
        print("|          ")
        print("|__________")
    else:
        print("________")
        print("|     |    ")
        print("|     O    ")
        print("|    /|\   ")
        print("|    / \    ")
        print("|          ")
        print("|__________")


guessWord = ["_" for letter in word]

while attempts < maxAttempts and "_" in guessWord:
    os.system("clear")
    print()
    print(
        "\033[38m \033[1mWelcome to Hangman! You have 6 attempts to guess the word!\033[0m")
    print(
        "\033[36m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m")
    hangmanDisplay(attempts)
    print(" ".join(guessWord))

    print()
    guess = input("Guess a letter: ").lower()

    if guess in guessedLetters:
        print()
        print("You already guessed that letter!")
        time.sleep(1)

    else:
        guessedLetters.append(guess)
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessWord[i] = guess
        else:
            attempts += 1

os.system("clear")
hangmanDisplay(attempts)
if "_" not in guessWord:
    print()
    print(
        f"\033[34m \033[1mCongratulations, you won! The word was \033[0m", word)
    print()
    print(f"\033[36m \033[1mYou had", attempts, "wrong guesses\033[0m")
    print()
    print("\033[35m \033[1mThank you for playing Hangman! I hope you enjoyed it! I had a lot of fun making it!\033[0m")
    print()
else:
    print()
    print(f"\033[31m \033[1mSorry, you lost. The word was\033[0m", word)
    print()
    print("\033[35m \033[1mThank you for playing Hangman! I hope you enjoyed it! I had a lot of fun making it!\033[0m")
    print()
