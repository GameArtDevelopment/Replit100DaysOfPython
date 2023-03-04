print("*****""\033[31m", "Generation Generator", "\033[0m""*****")
print()
name = input("What's you name?. ")
print()
print("Hi,", name, ",let's find out what generation you are.")
print()
year = int(input("What year were you born?. "))
print()
if (year <= 1945 and year >= 1925):
    print(name, ", you're a", "\033[35m", "Traditionalist.", "\033[0m")
elif (year >= 1946 and year <= 1964):
    print(name, ", you're a", "\033[36m", "Baby Boomer.", "\033[0m")
elif (year >= 1965 and year <= 1979):
    print(name, ", you're a", "\033[33m", "Generation X.", "\033[0m")
elif (year >= 1980 and year <= 1994):
    print(name, ", you're a", "\033[30m", "Millenial.", "\033[0m")
elif (year >= 1995 and year <= 2012):
    print(name, ", you're a", "\033[32m", "Generation Z.", "\033[0m")
elif (year >= 2013 and year <= 2025):
    print(name, ", you're a", "\033[34m", "Generation ALPHA.", "\033[0m")
print()
print("Thank you for trying my Generation Generator")
print()
