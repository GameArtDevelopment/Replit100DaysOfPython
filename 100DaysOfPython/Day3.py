print("=== Ultimate Wacky Recipe Maker ===")
print("""You'll be asked a few questions
then python we'll make your personal
recipe.""")
print()
name = input("What is your name? ")
food = input("What is your favorite food: ")
vegetable = input("What is your favorite vegetable: ")
cooking = input(
    "Which one of these three methods of cooking do you prefer? Fried, Steamed, Sauteed, or Barbecued: ")
burnt = input("Describe burned food: ")
item = input("What is your favorite household item? ")
print()
print("==== MENU ====")
print(name + "'s SPECIAL Meal")
print(cooking, burnt, food, " with", vegetable, "and a side of", item)
