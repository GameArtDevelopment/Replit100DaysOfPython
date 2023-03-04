import random

uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!\#$%&'()*+,-./:;<=>?@[]"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercaseLetters
if lower:
    all += lowercaseLetters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 10

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
