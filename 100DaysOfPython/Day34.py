import os
import time
import random

emails = []

customSpamEmails = ['sample1@example.com', 'sample2@example.com', 'sample3@example.com', 'sample4@example.com', 'sample5@example.com',
                    'sample6@example.com', 'sample7@example.com', 'sample8@example.com', 'sample9@example.com', 'sample10@example.com']


for email in customSpamEmails:
    emails.append(email)


spamMessages = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Proin et tellus eget eros pulvinar congue sed vel velit.",
    "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
    "Sed nec velit nunc. Suspendisse sed massa ullamcorper, ultrices elit non, blandit ante.",
    "Vivamus vehicula libero ac metus faucibus, in dignissim sapien imperdiet.",
    "Praesent aliquet eleifend nulla, eget consequat arcu vestibulum id.",
    "Integer sed justo id odio tristique ultricies quis eu dui.",
    "Donec bibendum mi vel tellus ornare posuere.",
    "Cras vitae tellus ut enim consequat bibendum non non sapien.",
    "Quisque et elit ut elit vehicula ultricies."
]


def addEmail():
    email = input("Enter email address: ")
    emails.append(email)
    print("Email added successfully.")


def removeEmail():
    email = input("Enter email address to remove: ")
    emails.remove(email)
    print("Email removed successfully.")


def viewEmails():
    print("List of emails:")
    for email in emails:
        print(email)


def spamEmails():
    for spam in customSpamEmails:
        os.system("clear")
        message = random.choice(spamMessages)
        print(f"Spam email sent to {spam}.")
        print(f"Message: {message}")
        time.sleep(2)
    print("10 emails were spammed today.")


while True:
    print("What would you like to do?")
    print("1. Add an email")
    print("2. Remove an email")
    print("3. View all emails")
    print("4. Spam emails")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        addEmail()
    elif choice == '2':
        removeEmail()
    elif choice == '3':
        viewEmails()
    elif choice == '4':
        spamEmails()
    elif choice == '5':
        print("Leaving App...")
        print()
        print("Thank you for using this app. I hope you enjoyed it!")
        break
    else:
        print("Invalid choice. Please try again.")
    time.sleep(1)
    os.system('clear')
