print()
print("\033[31m", "***HOW MANY SECONDS IN A YEAR****", "\033[0m")
secondsInYr = (((365 * 24)*60)*60)
additionalDay = ((24 * 60) * 60)
print()
print("Let's find out how many seconds are in a year")
print()
year = int(input("What year is it?. "))
print()
if year % 4 == 0:
    print("The year", "\033[32m", year, "\033[0m", "is a leap year, it has", "\033[36m",
          secondsInYr + additionalDay, "\033[0m", "seconds")
    print()
else:
    print("The year", "\033[33m", year, "\033[0m", "has" "\033[34m",
          secondsInYr, "\033[0m", "seconds")
    print()
print("Thank you for using my Python app.")
print()
