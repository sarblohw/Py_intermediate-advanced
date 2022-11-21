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

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#class variable can be accessed through class or through instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.__dict__)
print(emp_1.__dict__)