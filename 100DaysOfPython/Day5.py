print("**** \033[44m MARVEL MOVIE CHARACTER QUESTIONS \033[0m ****")
print()
print("This is a short Marvel Character questionaire, I hope you enjoy it!")
print()
skill = input("Do you like to read minds? yes or no: ")
print()
print("So,", skill, "you like to read minds, got it!")
print()
if (skill == "yes"):
    print("You are a telepath, like Professor X!")
else:
    print("DC, all the way!")

print()
friend = input("Is Wolverine your best friend? yes or no: ")
if (friend == "yes"):
    print("You are a mutant, like Wolverine!")
    print("The rest of the X-Men solute you!")
    print()

else:
    print("You are a human, like Captain America!")
    print("The rest of the Avengers solute you!")
    print()

print()

print("Thank you for trying my simple if/else statement!")
print("I hope you enjoyed it!")
print()
