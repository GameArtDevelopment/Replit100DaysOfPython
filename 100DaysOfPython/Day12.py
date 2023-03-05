print()
print("\033[31m", "****100 Days of Python Code QUIZ****", "\033[0m")
print()
print("How many can you answer correctly? ")
print()
ans1 = input("What language are we writing in? ").upper()
if ans1 == "PYTHON":
    print("Correct, you are writing in", "\033[32m", ans1, "\033[0m")
    print()
else:
    print("Nope")
    print()
ans2 = int(input("Which lesson number is this? "))
if (ans2 > 12):
    print()
    print("We're not quite that far yet")
    print()
elif (ans2 == 12):
    print()
    print("That's right!, we are on lesson", "\033[36m", ans2, "\033[0m")
    print()
else:
    print()
    print("We've gone well past that!")
    print()
print("Fixing these Python code errors went smoothly.")
print()
print("Thank you for checking out my progress.")
print()
