print()
print("\033[31m", "****GRADE CALCULATOR****", "\033[0m")
print()
name = input("What is your name: ")
print()
testName = input("What is the name of your exam? ")
print()
maxScore = float(input("What is the max score you could get on the exam? "))
print()
print("Great, the", testName, "exam has maximum score of", maxScore)
print()
testScore = float(input("How many points did you get? "))
print()
print("Okay, let's see what letter and percentage grade that is.")
grade = round((testScore / maxScore)*100, 2)
print()
print("\033[32m", "........", "\033[0m")
print()
print("\033[35m", "...........", "\033[0m")
print()
print("\033[33m", "Just a few more seconds.", "\033[0m")
print()
print("\033[31m", "..........Done!", "\033[0m")
print()
results = input("Press ENTER/RETURN to get your score.")
print()
if (grade >= 90 and grade <= 100):
    print(name, "\033[31m", "FANTASTIC JOB!", "\033[0m", "you scored an", "\033[31m", "A+", "\033[0m",
          "Your percentage score is:", "\033[31m", grade, "%", "\033[0m", "You are an elite student.")
elif (grade >= 80 and grade < 90):
    print(name, "\033[32m", "GREAT JOB!""\033[0m", "you scored an", "\033[32m", "A-", "\033[0m",
          "Your percentage score is:", "\033[32m", grade, "%", "\033[0m", "Hard work pays off.")
elif (grade >= 70 and grade < 80):
    print(name, ",that's a", "\033[33m", "GOOD GRADE!", "\033[0m", "you scored a", "\033[33m", "B",
          "\033[0m", "Your percentage score is:", "\033[33m", grade, "%", "\033[0m", "Keep up the good work.")
elif (grade >= 60 and grade < 70):
    print(name, ",that's an", "\033[34m", "OKAY GRADE!", "\033[0m", "you scored a", "\033[34m", "C", "\033[0m",
          "Your percentage score is:", "\033[34m", grade, "%", "\033[0m", "We have room for improvement.")
elif (grade >= 50 and grade < 60):
    print(name, ",this is not", "\033[35m", "NOT GOOD!""\033[0m", "you scored a", "\033[35m", "D", "\033[0m",
          "Your percentage score is:", "\033[35m", grade, "%", "\033[0m", "Schedule a meeting with me as soon as possible.")
elif (testScore < 50):
    print(name, ",this is", "\033[36m", "VERY BAD!", "\033[0m", "you scored a", "\033[36m", "F", "\033[0m", "Your percentage score is:",
          "\033[36m", grade, "%", "\033[0m", "Expect a call home, and we must schedule a meeting with your guardians.")
else:
    print("I don't know what exam you took, but that exam did not have extra credit. Please run the program again. Thank you.")
print()
print("Thank you for trying my GRADE CALCULATOR.")
print()
