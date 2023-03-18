from replit import audio
import os
import time


def play():
    source = audio.play_file('audio.wav')
    source.paused = False  # unpause the playback
    while True:
        stopPlay = int(
            input("Press 2 to stop playback and open Music Player's Main Menu: "))
        if stopPlay == 2:
            source.paused = True
            return
        else:
            continue


while True:
    os.system("clear")
    print("\033[34m🎻MyPOD Music Player🎹\033[0m")
    time.sleep(2)
    print("Press 1 to Play")
    time.sleep(1)
    print("Press 2 to Exit")
    time.sleep(2)
    print("Press any other number to open Music Player's Main Menu")
    userInput = int(input())
    if userInput == 1:
        print("Playing some Replit 🎹tunes🎻")
        play()
    elif userInput == 2:
        exit()
    else:
        continue
