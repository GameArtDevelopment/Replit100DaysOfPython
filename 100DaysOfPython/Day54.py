# You will need to create a csv file called Day54Totals.csv
import csv

total_earnings = 0

with open('Day54Totals.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cost = float(row['Cost'])
        quantity = int(row['Quantity'])
        earnings = cost * quantity
        total_earnings += earnings
print("="*25)
print("*\033[34m      Nebula Games\033[0m     *")
print("="*25)
print("Public record of earnings")
print()
print("* \033[31mExtrada2D Earnings\033[0m *")
print("="*22)
print()
print(
    f"The indie game \033[32mExtrada2D\033[0m earned \033[32m${total_earnings:.2f}\033[0m during it's first month on steam.")
print()
print("* \033[31mIsland Odyssey: The Quest for the Lost Relics\033[0m *")
print("="*60)
print("Release date: 07/01/2023")
print()
print("Thank you for your support!")
print("I hope you enjoyed this simple csv reader.")
print()
