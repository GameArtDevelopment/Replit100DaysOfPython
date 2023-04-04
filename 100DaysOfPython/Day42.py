print()
print("\033[36m=========================\033[0m")
print("* Welcome to PrezBeast! *")
print("\033[35m=========================\033[0m")
print()
prezdex = {
    "Beast Name": "",
    "Type": "",
    "Special Move": "",
    "HP": "",
    "MP": ""
}

print("PrezBeast\n")

for key in prezdex:
    prezdex[key] = input(f"{key}: ").strip().title()

typeColor = {
    "Earth": "\033[32m",
    "Air": "\033[33m",
    "Fire": "\033[31m",
    "Water": "\033[34m",
    "Spirit": "\033[35m"
}

print()
print(f"{typeColor[prezdex['Type']]}Beast Name: {prezdex['Beast Name']}")
print(f"Type: {prezdex['Type']}")
print(f"Special Move: {prezdex['Special Move']}")
print(f"HP: {prezdex['HP']}")
print(f"MP: {prezdex['MP']}")
print("\033[0m")
print()
print("Thank you for using PrezBeast!")
print()
