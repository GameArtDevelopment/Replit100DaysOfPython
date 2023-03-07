print("\033[31m", "****WHILE LOOP****", "\033[0m")
print()
print("Hi user, this is my poor attempt at Day 15 while loop challenge.")
print()
print("Sorry, but you can only pick the animals in this order -> ",
      "\033[34m", "Cow, Cat, Dog, and Bird.", "\033[0m")
print()
animal = input("What animal sound do you want?: ").lower()

while animal == "cow" or animal != "yes":
    print("Cow goes moo")
    animal = input("Exit: ? or What animal sound do you want?: ").lower()
    print()
    if (animal == "cat"):
        print("Cat goes meow")
        animal = input("Exit: ? or What animal sound do you want?: ").lower()
        print()
        if (animal == "dog"):
            print("Dog goes woof")
            animal = input(
                "Exit: ? or What animal sound do you want?: ").lower()
            print()
            if (animal == "bird"):
                print("Bird goes tweet")
                animal = input(
                    "Exit: ? or What animal sound do you want?: ").lower()

print()
print("You've exited the while loop. Thanks for playing")
print()
print("Thank you for trying my while loop.")
print()
