import os


def palidrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return palidrome(word[1:-1])


while True:
    os.system("clear")
    print("\033[32m=\033[0m"*37)
    print("* Welcome to the palindrome checker *")
    print("\033[36m=\033[0m"*37)
    print()
    word = input("Enter a word: ")
    if palidrome(word):
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

    play = input("Do you want to play again? (y/n): ")
    if play.lower() == "n":
        break
print()
print("Thanks for playing!")
print()
