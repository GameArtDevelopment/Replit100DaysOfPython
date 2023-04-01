import os
import time
print(" ========================================")
print("         Welcom to my Calculator!")
print(" ========================================")
print()
print("This calculator can add, subtract, multiply, and divide.")
print()
print("Please enter the first number.")
print()
firstNumber = int(input("First Number: "))
print()
print("Please enter the second number.")
print()
secondNumber = int(input("Second Number: "))
print()
print("Please enter the operation you would like to perform.")
print()
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print()
operation = int(input("Operation: "))
print()
if operation == 1:
    os.system("clear")
    print("The sum of {} and {} is {}.".format(
        firstNumber, secondNumber, firstNumber + secondNumber))
    print()
elif operation == 2:
    os.system("clear")
    print("The difference of {} and {} is {}.".format(
        firstNumber, secondNumber, firstNumber - secondNumber))
    print()
elif operation == 3:
    os.system("clear")
    print("The product of {} and {} is {}.".format(
        firstNumber, secondNumber, firstNumber * secondNumber))
    print()
elif operation == 4:
    os.system("clear")
    print("The quotient of {} and {} is {}.".format(
        firstNumber, secondNumber, firstNumber / secondNumber))
    print()
else:
    print("Invalid operation.")
    print()
print("Thank you for using my Calculator!")
print()
