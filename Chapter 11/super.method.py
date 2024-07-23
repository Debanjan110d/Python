class Employee:
    a =10
    def __init__(self) :
       print("Constructor Of Employee")

class Coder(Employee):
    b = 20
    def __init__(self) :
       print("Constructor Of Coder")

class Programer(Coder):
    c = 30
    def __init__(self) :
       print("Constructor Of Programer")
       super().__init__()

p = Programer()
print(p.a)
print(p.b)
print(p.c)