import random

print()
print("\033[34m============ Welcome to the Greeting Generator! ============\033[0m")

greeting = ["Guten Tag", "Hello", "Privet", "Nǐ hǎo", "Ciao", "Konnichiwa",
            "Shalom", "Bonjour", "Goddag", "Namaste, Namaskar", "God dag"]

choices = random.randint(0, 11)

response = (f"Greeting: \033[32m{greeting[choices]}\033[0m")

print()
print(f"{response:^67}")

print()
print("\033[34m==============   Thank you trying my code    ===============\033[0m")
print()
