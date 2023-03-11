print("\033[31m")
print("        ********************************       ")
print("        *                              *       ")
print("        * A SIMPLE INTEREST CALCULATOR *       ")
print("        *                              *       ")
print("        ********************************       ")
print("\033[0m")
print()
print("A Python code calculates how much 5% APR will cost.")
print()
borrowed = int(input("How much money do you want to borrow? "))
print()
years = 10
apr = 0.05
for i in range(years):
    borrowed = borrowed * (1 + apr)
    print("On year", i+1, "you will owe: $",
          "\033[32m", round(borrowed, 2), "\033[0m")
print()
print("Your total damage on $1000 at 5% APR for 10 years is: $",
      "\033[32m", round(borrowed, 2), "\033[0m")
print()
print("Thank you for trying my Day 19 challenge.")
print()
