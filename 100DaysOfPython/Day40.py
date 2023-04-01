import os
contact = {}
print("\033[34m========================================\033[0m")
print("* Welcome to the Contact Card Creator! *")
print("\033[34m========================================\033[0m")
print()
name = input("What is your name? ").strip()
dob = input("What is your date of birth? ").strip()
telephone = input("What is your telephone number? ").strip()
email = input("What is your email address? ").strip()
address = input("What is your physical address? ").strip()
os.system("clear")
contact["Name"] = name
contact["Date of Birth"] = dob
contact["Telephone"] = telephone
contact["Email"] = email
contact["Address"] = address
print()
print("""\033[32mContact Card\033[0m
------------
\033[34mName:\033[0m {}
\033[34mDate of Birth:\033[0m {}
\033[34mTelephone:\033[0m {}
\033[34mEmail:\033[0m {}
\033[34mAddress:\033[0m {}
""".format(contact["Name"], contact["Date of Birth"], contact["Telephone"], contact["Email"], contact["Address"]))

print("Thank you for using my Contact Card Creator!")
print()
