# class Employee:
#     a =10
#     def show(self) :
#        print(f"Constructor Of Employee {self.a}")

# e = Employee()
# e.a =100
# e.show()

class Employee:
    a =10
    @classmethod
    def show(cls) :
       print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a =100
e.show()
