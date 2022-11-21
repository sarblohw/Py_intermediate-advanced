class Employee:

    raise_amount = 1.04

    def __init__(self, f_name, l_name, comp):
        self.first = f_name
        self.last = l_name
        self.pay = comp

    def full_name(self):
        return f'{self.first.title()} {self.last.title()}'

    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) 
        #class variable can be accessed through class or through instance

emp_1 = Employee('suminder', 'singh', 250000)
emp_2 = Employee('test', 'user', 75000)

#class variable can be accessed through class or through instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#setting class variable/attribute
#when attribute called by instance, it will first check if the instance has that attribute and if not, it will check class for the same thing
emp_1.raise_amount = 1.50

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)
print(emp_2.__dict__)
#the instance namespace for emp_1 now has the attribute raise_amount