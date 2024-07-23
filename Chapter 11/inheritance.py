class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")
# class Programer :
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")
#     def show(self):
#         print(f"The name is {self.name} and proficient in  {self.language}")

class Coder:
    language = "js"
    def printLanguages(self):
        print(self.language)

class Programer(Employee,Coder):
    company = "Jis"
    def show(self):
        print(f"The name is {self.name} and proficient in  {self.language}")

e = Employee()
e.name = "Huha"
e.salary = 200
print(e.company)
e.show()

p = Programer()
p.name = "Ravi"
p.salary = 100
p.language = "Python"
print(p.company)
p.show()
p.printLanguages()
