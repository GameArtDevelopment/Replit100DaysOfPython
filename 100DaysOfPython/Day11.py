print("***How many seconds in a year?.****")
secondsInYr = (((365 * 24)*60)*60)
additionalDay = ((24 * 60) * 60)
print()
year = int(input("What year is it?. "))
print()
if year % 4 == 0:
    print("This is a leap year, we have ",
          secondsInYr + additionalDay, "seconds")
    print()
else:
    print("This year, we have ", secondsInYr, "seconds")
    print()
print("Thank you for using my Python app.")
print()
