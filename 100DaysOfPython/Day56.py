import csv
import os
# Function to create the folders for each artist


def create_artist_folders():
    # Open the CSV file containing the song data
    with open('100MostStreamedSongs.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Loop through each row in the CSV file
        for row in reader:
            # Extract the artist and song title from the row
            artist = row['Artist(s)']
            song_title = row['Song']
            # Create the folder for the artist if it doesn't already exist
            if not os.path.exists(artist):
                os.mkdir(artist)
            # Create the text file for the song in the artist's folder
            with open(os.path.join(artist, song_title + '.txt'), 'w', encoding='utf-8') as f:
                f.write('')  # write an empty string to the file
    print("Artist folders created successfully!")
    os.system('clear')
# Function to display the list of songs by title


def display_songs_by_title():
    # Open the CSV file containing the song data
    with open('100MostStreamedSongs.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Loop through each row in the CSV file and print the song title
        for row in reader:
            song_title = row['Song']
            print(song_title)
# Main function that displays the menu and handles user input


def main():
    while True:
        print("\033[33m=\033[0m"*32)
        print("* Welcome to the Song Library! *")
        print("\033[34m=\033[0m"*32)
        print("1. Create artist folders")
        print("2. View list of songs by title")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_artist_folders()
        elif choice == '2':
            display_songs_by_title()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
    print()
    print("Goodbye!")


# Call the main function
main()
print()
print("Thank you for using my Song Library using directories and csv file!")
