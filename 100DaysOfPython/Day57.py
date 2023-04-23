print("\033[33m=\033[0m"*40)
print("* Welcome to the factorial calculator! *")
print("\033[36m=\033[0m"*40)
print()
print("This program will calculate the factorial of a number using recursion.")
print()


def factorialMultiplication(n):
    """
    This function starts at the highest number, multiplies it by factorial of itself minus one, and
    terminates when it reaches 1 and returns 1. It then outputs the factorial.
    """
    if n == 1:
        print(f"\033[30mFactorial of {n}\033[0m = \033[35m1\033[0m")
        return 1
    else:
        result = n * factorialMultiplication(n - 1)
        print(f"\033[30mFactorial of {n}\033[0m = \033[35m{result}\033[0m")
        return result


n = int(input("Enter a number: "))
print()
result = factorialMultiplication(n)
print()
print(f"\033[34mThe factorial of {n} is \033[0m \033[31m{result}\033[0m")
print()
print("Thank you for using my factorial calculator!")
print()
