import datetime
import os


def loadEvents():
    """Load saved events from a text file."""
    events = {}
    if os.path.isfile('events.txt'):
        with open('events.txt', 'r') as f:
            for line in f:
                eventName, eventDateString = line.strip().split(',')
                eventDate = datetime.datetime.strptime(
                    eventDateString, '%Y-%m-%d').date()
                events[eventName] = {
                    'name': eventName, 'date': str(eventDate)}
    return events


def saveEvents(events):
    """Save events to a text file."""
    with open('events.txt', 'w') as f:
        for event in events.values():
            f.write(f"{event['name']},{event['date']}\n")


def createEvent():
    """Create a new event."""
    # Prompt user to input event name and date
    eventName = input("Enter the name of your event: ")
    eventDateString = input("Enter the date of your event (YYYY-MM-DD): ")

    # Convert event date string to a date object
    eventDate = datetime.datetime.strptime(eventDateString, '%Y-%m-%d').date()

    return {'name': eventName, 'date': str(eventDate)}


def showEvent(events):
    """Display a list of saved events."""
    if events:
        for eventName, event in events.items():
            eventDate = datetime.datetime.strptime(
                event['date'], '%Y-%m-%d').date()
            days_until_event = (eventDate - datetime.date.today()).days
            if days_until_event > 0:
                print("="*19)
                print("\033[33m*  Future Events  *\033[0m")
                print("="*19)
                print(
                    f"{eventName}: {days_until_event} days until {event['date']}")
            elif days_until_event == 0:
                print("="*20)
                print("\033[36m*  Today's Events  *\033[0m")
                print("="*20)
                print(f"{eventName}: Today is {event['date']}!")
            else:
                print("="*19)
                print("\033[31m*   Past Events   *\033[0m")
                print("="*19)
                print(
                    f"{eventName}: {abs(days_until_event)} days ago ({event['date']})")
            input("Press Enter to continue...")
            print()
    else:
        print("No saved events.")


def mainMenu():
    """Display the main menu and handle user input."""
    events = loadEvents()
    while True:
        os.system("clear")
        print("\033[32m=\033[0m"*19)
        print("   * Main Menu *")
        print("\033[35m=\033[0m"*19)
        print("1. Create a new event")
        print("2. Show saved events")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            event = createEvent()
            events[event['name']] = event
            print(f"Event '{event['name']}' has been created.")
        elif choice == '2':
            showEvent(events)
        elif choice == '3':
            saveEvents(events)
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")
    print()


mainMenu()
