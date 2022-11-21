class Employee:

    def __init__(self, f_name, l_name, comp):
        self.first = f_name
        self.last = l_name
        self.pay = comp
        self.email = f'{f_name.lower()}.{l_name.lower()}@company.com'

emp_1 = Employee('suminder', 'singh', 250000)
emp_2 = Employee('test', 'user', 75000)

print(emp_1.first, emp_1.email, emp_2.email)