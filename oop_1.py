class Employee:
        def __init__(self, first, last, pay):
            self.fname = first
            self.lname = last
            self.email = first + "." + last + "@company.com"
            self.salary = pay

emp_1 = Employee('Suminder', 'Singh', 100000)
print(emp_1.lname)
print(emp_1.email)
