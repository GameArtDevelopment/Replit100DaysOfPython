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
                    eventDateString, '%m-%d-%Y').date()
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
    eventDateString = input("Enter the date of your event (MM-DD-YYYY): ")

    # Convert event date string to a date object
    eventDate = datetime.datetime.strptime(eventDateString, '%m-%d-%Y').date()

    return {'name': eventName, 'date': str(eventDate)}


def editEvent(events):
    """Edit an existing event."""
    eventName = input("Enter the name of the event to edit: ")
    if eventName in events:
        newEvent = createEvent()
        events[eventName] = newEvent
        print(f"Event '{eventName}' has been updated.")
    else:
        print(f"Event '{eventName}' not found.")


def showEvent(events):
    """Display a list of saved events."""
    if events:
        print("Saved Events:")
        for eventName, event in events.items():
            eventDate = datetime.datetime.strptime(
                event['date'], '%Y-%m-%d').date()
            days_until_event = (eventDate - datetime.date.today()).days
            if days_until_event > 0:
                print(
                    f"{eventName}: {days_until_event} days until {event['date']}")
            elif days_until_event == 0:
                print(f"{eventName}: Today is {event['date']}!")
            else:
                print(
                    f"{eventName}: {abs(days_until_event)} days ago ({event['date']})")
    else:
        print("No saved events.")


def mainMenu():
    """Display the main menu and handle user input."""
    events = loadEvents()
    while True:
        os.system("clear")
        print("\033[32m=\033[0m"*19)
        print("   * Main Menu *")
        print("\033[36m=\033[0m"*19)
        print("1. Create a new event")
        print("2. Edit an existing event")
        print("3. Show saved events")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            event = createEvent()
            events[event['name']] = event
            print(f"Event '{event['name']}' has been created.")
        elif choice == '2':
            editEvent(events)
        elif choice == '3':
            showEvent(events)
        elif choice == '4':
            saveEvents(events)
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")
    print()


mainMenu()
