print("\033[31m", "****Bill Calculator****", "\033[0m")
print()
bill = float(input("What is the bill amount?: "))
print()
percentage = float(input("What percentage of tip would you like to leave?. "))
print()
numberOfPeople = int(input("How many people?: "))
print()
answer = bill / numberOfPeople
answer = round(answer, 2)
tip = round(percentage * bill) / 100
totalBill = round(bill + tip)
indiBill = round((bill + tip) / numberOfPeople)
plus1 = round(indiBill * 2)
print("You each owe", "\033[32m","$",answer, "\033[0m",
      "and your total tip is", "\033[33m","$",tip, "\033[0m")
print()
print("Your total bill is", "\033[34m","$",totalBill, "\033[0m")
print()
print("Including tip, each person's owes", "\033[35m","$",indiBill, "\033[0m")
print()
print("But because you brought your broke friend, you owe",
      "\033[36m","$",plus1, "\033[0m")
print()
