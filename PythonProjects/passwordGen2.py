import random
import string
# Define the ANSI escape code for bold text
bold = "\033[1m"
while True:
    # Define the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    print()
    print("\033[32m=\033[0m"*22)
    print("* Password Generator *")
    print("\033[33m=\033[0m"*22)
    # Prompt the user to specify the password criteria
    use_uppercase_letters = input("Use uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase_letters = input("Use lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Use digits? (y/n): ").lower() == 'y'
    use_symbols = input("Use symbols? (y/n): ").lower() == 'y'
    password_length = int(input("Password length (minimum 8): "))
    # Validate the password length
    if password_length < 8:
        password_length = 8
        print("Password length set to minimum of 8")

    num_passwords = int(input("Number of passwords to generate: "))
    # Combine the character sets based on the criteria
    character_set = ''
    if use_uppercase_letters:
        character_set += uppercase_letters
    if use_lowercase_letters:
        character_set += lowercase_letters
    if use_digits:
        character_set += digits
    if use_symbols:
        character_set += symbols
    # Generate the passwords
    for i in range(num_passwords):
        password = ''.join(random.choice(character_set) for _ in range(password_length))
        print(f"{bold}{password}\033[0m")

    # Ask the user if they want to generate another set of passwords
    response = input("Generate another set of passwords? (y/n): ").lower()
    if response != 'y':
        break
