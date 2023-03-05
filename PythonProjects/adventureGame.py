print("****Chose Your Own Adventure****")
print()
name = input("What is your name? ")
print()
print("Welcome", name, "to the adventure!")
print()
answer = input(
    "You are at a fork on the road. Will you go left or right? ").lower()
print()
if answer == "left":
    answer = input(
        "You reach the end of the road and reach a cabin. Do you go in or turn around? ").lower()
    if answer == "go in":
        print("You entered the cabin and never came back.")
    elif answer == "turn around":
        print("You went back to the fork and went right and a man grabs you. You lose!")
    else:
        print("Not a valid answer. Please try again.")
elif answer == "right":
    answer = input(
        "You reach the end of the road and find yourself in the forest. A bear chased you and you have to escape up the mountain or down to the river. ").lower()
    if answer == "up the mountain":
        print("You escaped. You won!")
    elif answer == "to the river":
        answer = input(
            "You find a boat. Will you get in or keep walking? ").lower()
        if answer == "get in":
            print("You entered the boat and never came back.")
        elif answer == "keep walking":
            print("You keep walking and find the secret gold. You won!")
    else:
        print("Not a valid answer. Please try again.")
else:
    print()
    print("Not a valid answer. Please try again.")
    print()
print("Thanks for playing,", name)
