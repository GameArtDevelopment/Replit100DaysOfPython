print("Welcome to my Python Quiz game!")
print("I hope you enjoyed it!")
print()
playing = input("Would you like to play? (yes/no) ")
if (playing != "yes"):
    quit()

print("Great! Let's play!")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect!")
    answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect!")
    answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect!")
    answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect!")
    answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect!")
print()
print("You scored " + str(score) + " out of 5 questions!")
print("Your percentage is ", str((score/5)*100), "%")
print()
