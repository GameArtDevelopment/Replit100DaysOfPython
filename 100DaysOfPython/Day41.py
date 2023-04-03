
websiteInfo = {}

websiteInfo.update({"myValue": None})
print()
print("Welcome to my website rating app!")
print()
print("===================")
print("🌟 Website Rating 🌟")
print("===================")
print()
for key in ['name', 'URL', 'description', 'rating']:
    value = input(f"Input the {key}: ")
    websiteInfo[key] = value
print()

for name, value in websiteInfo.items():
    print(f"{name}: {value}")

print()
print("Thank you for using my website rating app!")
print()
