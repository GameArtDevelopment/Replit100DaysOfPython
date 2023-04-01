import os
import time
print("==============================================")
print("* Welcome to my Interest Payment Calculator! *")
print("==============================================")
print()
print("Please enter the amount of money you would like to borrow.")
print()
borrow = float(input("Borrow: $").strip())
print()
print("Please enter the interest rate.")
print()
interest = float(input("Interest: ").strip())
print()
print("Please enter the number of years you would like to borrow for.")
print()
years = float(input("Years: ").strip())
print()
print("Calculating interest...")
print()
time.sleep(1)
os.system("clear")
interest = interest / 100
interest = interest / 12
interest = interest + 1
interest = interest ** 12
interest = interest - 1
interest = interest * borrow
interest = interest * years
interest = interest + borrow
interest = round(interest, 2)
print("The total amount you will pay back is: $" + str(interest))
print()
print("Thank you for using my Interest Payment Calculator!")
print()
