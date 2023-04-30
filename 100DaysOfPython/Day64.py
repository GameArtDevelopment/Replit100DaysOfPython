class Job:
    def __init__(self, name, salary, hours_worked):
        self.name = name
        self.salary = salary
        self.hours_worked = hours_worked

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Hours worked: {self.hours_worked}")


class Doctor(Job):
    def __init__(self, name, salary, hours_worked, speciality, years_of_experience):
        super().__init__(name, salary, hours_worked)
        self.speciality = speciality
        self.years_of_experience = years_of_experience

    def print_details(self):
        super().print_details()
        print(f"Speciality: {self.speciality}")
        print(f"Years of experience: {self.years_of_experience}")


class Teacher(Job):
    def __init__(self, name, salary, hours_worked, subject, position):
        super().__init__(name, salary, hours_worked)
        self.subject = subject
        self.position = position

    def print_details(self):
        super().print_details()
        print(f"Subject: {self.subject}")
        print(f"Position: {self.position}")


lawyer = Job("John Smith", 100000, 40)
computer_teacher = Teacher("Alice Johnson", 60000,
                           35, "Computer Science", "Full-time")
pediatric_doctor = Doctor("Mark Davis", 150000, 50, "Pediatrics", 7)
print("Lawyer:")
lawyer.print_details()
print()
print("Computer Science Teacher:")
computer_teacher.print_details()
print()
print("Pediatric Doctor:")
pediatric_doctor.print_details()
