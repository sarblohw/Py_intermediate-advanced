class Employee:

    def __init__(self, f_name, l_name, comp):
        self.first = f_name
        self.last = l_name
        self.pay = comp

    def full_name(self):
        return f'{self.first.title()} {self.last.title()}'

    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    def apply_raise(self):
        self.pay = int(self.pay * 1.04) #hardcoded the raise amount

emp_1 = Employee('suminder', 'singh', 250000)
emp_2 = Employee('test', 'user', 75000)

print(emp_1.first, emp_1.pay)
emp_1.apply_raise()
print(emp_1.first, emp_1.pay)