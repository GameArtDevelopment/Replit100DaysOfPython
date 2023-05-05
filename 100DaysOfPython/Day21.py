import os
import time
print("\033[34m")
print("        ********************************       ")
print("        *                              *       ")
print("\033[0m,\033[31m       *   WELCOME TO MATH CHALLENGE  *\033[0m       ")
print("\033[34m        *                              *       ")
print("        ********************************       ")
print("\033[0m")
print()
counter = 0
num = 0
print("This is the Multiplication Math Challenge")
print()
num = int(input("Enter the number you wish to be challeged on: "))
for i in range(1, 11):
    os.system("clear")
    ans = i * num
    print("\033[34m", i, "X", num, "=", "\033[0m")
    response = int(input("What's the answer? "))
    if (response == ans):
        print()
        print("GOOD JOB!")
        time.sleep(1)
        print()
        counter += 1
    else:
        print()
        print("YOU MISSED THAT ONE!")
        time.sleep(1)
        print()
if (counter == 10):
    print()
    print("You scored a perfect", "\033[33m", counter, "\033[0m",
          "🥳 You are a Math Genius!💪🏻")
elif (counter >= 5 and counter < 10):
    print()
    print(
        "You scored", "\033[32m", counter, "\033[0m", "out of 10. That was a good score. Study more; I guarantee you will get a better score next time."
    )
elif (counter < 5):
    print()
    print("You scored", "\033[31m", counter, "\033[0m",
          "out of 10. That was not a good score.")
print()
print("Thank you for trying the Math Challenge.")
print()
