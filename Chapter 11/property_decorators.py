class Employee:
    a = 10

    @classmethod
    def show(cls):
       print(f"The class attribute of a is {cls.a}")

    def __init__(self):
        self.fname = None
        self.lname = None

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        fname, lname = value.split(" ")
        self.fname = fname
        self.lname = lname


e = Employee()
e.name = "Debanjan Dutta"
print(e.fname, e.lname)
e.show()