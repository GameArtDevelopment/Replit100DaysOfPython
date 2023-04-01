# importing time library
import time

# defining the countdown function. taking parameter t
print("\033[35m+++++++++++++++++++++++++++++++++++++++++\033[0m")
print("+++++++++++++    \033[31mPOMODORO\033[0m     +++++++++++")
print("\033[35m+++++++++++++++++++++++++++++++++++++++++\033[0m")


def countdown(t):
    while t:  # as long as t is not 0
        mins, secs = divmod(t, 60)  # divmod returns quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs)  # formatting the timer
        print(timer, end="\r")  # printing the timer
        time.sleep(1)  # pausing the code for 1 second
        t -= 1  # decrementing t by 1
    print()
    print("Pomodoro Complete!")  # printing the message when t is 0
    print()


print()
t = input("Enter how many minutes: ")  # taking input from user

# choices make t into 10minutes, 20minutes, 30minutes, 40minutes, 50minutes, 60minutes
if t == "1":
    t = 60
elif t == "10":
    t = 600
elif t == "20":
    t = 1200
elif t == "30":
    t = 1800
elif t == "40":
    t = 2400
elif t == "50":
    t = 3000
elif t == "60":
    t = 3600


# calling the function and passing the user input as an argument
countdown(int(t))

print("Credits to: Code With Tomi.")
