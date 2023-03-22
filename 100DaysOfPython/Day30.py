import os
import time
print("\033[31m*******  30 DAY QUESTIONNAIRE  *******\033[0m")
print()
for i in range(1, 31):
    answer = input(f"How was Day {i}?: ")
    os.system("clear")
    print()
    statement = (f"\033[32mDay {i}:\033[0m \033[34m{answer}\033[0m")
    print()
    time.sleep(.5)
    print(statement)
    print()
    print(
        "\033[31m------------------------------------------------------------\033[0m")
    print()
print("\033[31m*******  END OF 30 DAY QUESTIONNAIRE  *******\033[0m")
print()
print("Thank you for taking the time to try my 30 Day questionnaire program.")
print()
