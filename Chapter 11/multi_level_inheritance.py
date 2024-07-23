class Employee:
    a =10

class Coder(Employee):
    b = 20

class Programer(Coder):
    c = 30

p = Programer()
print(p.a)
print(p.b)
print(p.c)