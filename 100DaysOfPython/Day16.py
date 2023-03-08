print("\033[31m", "****FIND THE MISSING LYRIC!****", "\033[0m")
print()
print("Type in the missing lyric.")
lyric = "It's the eye of the _____. "
counter = 0
print()
while True:
    print("")
    word = input(lyric + "What's the missing lyric?: ").lower()
    counter += 1
    if (word == "tiger"):
        break
if (counter == 1):
    print()
    print("\033[33m", "Incredible!", "\033[0m", " it only took you", "\033[35m", counter, "\033[0m",
          "attempt to figure it out. Consider yourself a lyrical superstar.")
elif (counter <= 3):
    print()
    print("Good Job! It only took you",
          "\033[32m", counter, "\033[0m", " attempts.")
else:
    print()
    print("Needs improvement!! It took you", "\033[34m", counter, "\033[0m",
          " attempts to figure out the lyric.")
    print("Better luck next time.")
print()
print("Thank you for trying my While True Loop. I hope you enjoyed yourself.")
print()
print("\033[31m", "It's the eye of the tiger")
print("it's the thrill of the fight")
print("Rising up to the challenge of our rival")
print("And the last known survivor")
print("Stalks his prey in the night")
print("And he's watching us all with the eye of the tiger", "\033[0m")
print()
print("Survivor - Eye of the Tiger")
print()
