print()
print("\033[31m *** Bill Splitter *** \033[0m")
print()
bill = float(input("What is the total bill? $"))
print()
percentage = float(input("What percentage of tip would you like to leave? "))
print()
numOfPeople = int(input("How many people to split the bill? "))
print()
ans = bill / numOfPeople
answer = round(ans, 2)
tip = round(percentage * bill) / 100
totalBill = round(bill + tip)
indiBill = round((bill + tip) / numOfPeople)
plus1 = round(indiBill * 2)
print("You each owe", "\033[32m", "$", answer, "\033[0m",
      "and your total tip is", "\033[32m", "$", tip, "\033[0m")
print()
print("Your total bill is", "\033[32m", "$", totalBill, "\033[0m")
print()
print("Including the tip, each person owes",
      "\033[32m", "$", indiBill, "\033[0m")
print()
print("But because you brought your broke friend, you owe",
      "\033[32m", "$", plus1, "\033[0m")
print()
print("Thanks for using the Bill Splitter!")
