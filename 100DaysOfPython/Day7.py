favorite = input("Are your a Marvel Super Fan?. ")
print()
if (favorite == "yes"):
    mutant = input(
        "Oh yeah! tell me which mutant has healing powers and claws that come out of his hands?. ")
    print()
    if (mutant == "wolverine"):
        print("lucky guess.")
        print()
        print("Thanks for playing my question generator.")
if (favorite == "no"):
    DC = input(
        "Oh, so you must be a DC fan boy. Is Superman your favorite DC heroe?. ")
    print()
    if (DC == "yes"):
        print("Me too!")
        print()
        print("I appreciate you playing my question generator, even if you're a DC person.")
    elif (DC == "no"):
        print(
            "Seriously!?, I need to add more question to my generator. Thanks for playing.")
    else:
        print()
        print("You need to become a fan boy, and answer these questions with yes or no.")
