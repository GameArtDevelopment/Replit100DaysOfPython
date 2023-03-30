print()
print("\033[36m============================================\033[0m")
print("* \033[33m\033[1m       Welcome to Rainbow Sentence!\033[0m      *")
print("\033[36m============================================\033[0m")
letters = ['r', 'b', 'g', 'p', 'y']
sent = input("Write a short sentence. ")

for letters in sent:
    if letters.lower() == "r":
        print("\033[31m", end='')
    elif letters.lower() == "b":
        print("\033[34m", end='')
    elif letters.lower() == "g":
        print("\033[32m", end='')
    elif letters.lower() == "p":
        print("\033[35m", end='')
    elif letters.lower() == "y":
        print("\033[33m", end='')
    elif letters.lower() == " ":
        print("\033[0m", end='')
    print(letters, end="")
