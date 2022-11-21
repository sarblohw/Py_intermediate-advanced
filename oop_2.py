class Employee:

    def __init__(self):
        pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Suminder'
emp_1.last = 'Singh' 
emp_1.email = 'suminder.singh@aexp.com'
emp_1.pay = 200000

emp_2.first = 'Test'
emp_2.last = 'User' 
emp_2.email = 'test.user@aexp.com'
emp_2.pay = 200000

print(emp_1.first, emp_1.email, emp_2.email)