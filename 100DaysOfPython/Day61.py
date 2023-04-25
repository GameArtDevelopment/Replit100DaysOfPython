import datetime
import os
import time

tweets = {}

while True:
    # Display menu
    print("=" * 34)
    print("\033[34m*    Welcome my BlueBird app!    *\033[0m")
    print("=" * 34)
    print()
    print(f"{'Menu:': >16}")
    print(f"{'1. Add tweet': >23}")
    print(f"{'2. View tweets': >25}")
    print(f"{'3. Exit': >18}")
    print()
    choice = input("Enter your choice: ")

    if choice == "1":
        # Get tweet input
        tweet = input("Enter your tweet: ")

        # Store tweet with current timestamp as key
        timestamp = datetime.datetime.now()
        tweets[timestamp] = tweet

        print("Tweet added successfully!")
        time.sleep(1)

    elif choice == "2":
        # Show tweets in chronological order with pagination
        sorted_tweets = sorted(tweets.items())
        tweet_count = len(sorted_tweets)
        page = 1
        page_count = (tweet_count - 1) // 10 + 1

        while True:
            # Display page header
            print(f"Page {page}/{page_count}:")
            print("-" * 50)

            # Display tweets for current page
            for i in range((page - 1) * 10, min(page * 10, tweet_count)):
                timestamp, tweet = sorted_tweets[i]
                print(f"[{timestamp}] {tweet}")

            print("-" * 50)

            # Prompt user to show next page or go back to menu
            if page < page_count:
                choice = input(
                    "Press enter/return to show the next page, or enter 'm' to go back to the main menu: ")

                if choice.lower() == "m":
                    break

                # Clear terminal screen before showing next page
                os.system('cls' if os.name == 'nt' else 'clear')
                page += 1

            else:
                choice = input(
                    "Press enter/return to go back to the main menu: ")

                if choice:
                    break

                # Clear terminal screen before going back to main menu
                os.system('cls' if os.name == 'nt' else 'clear')
                break

    elif choice == "3":
        # Exit program
        print()
        print("Goodbye!")
        print("Try entering more than 10 tweets to see pagination in action.")
        print()
        print("Thank you for using my BlueBird app!")
        break

    else:
        print("Invalid choice. Please try again.")

    # Clear terminal screen before showing menu again
    os.system('cls' if os.name == 'nt' else 'clear')
