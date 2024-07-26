class Employee:
    salary = 30000
    increment  =15

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,nsalary):       
        self.increment = ((nsalary - self.salary)/self.salary)*100


e = Employee()

print(e.salaryAfterIncrement)
print(e.increment)

e.salaryAfterIncrement = 50000


print(e.increment)