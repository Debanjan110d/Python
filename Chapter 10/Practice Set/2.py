class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2
    
    def square(self):
        return self.num1 * self.num1
    
    def cube(self):
        return self.num1 * self.num1 * self.num1
    
    def power_of(self):
        return self.num1 ** self.num2
    
    def mod(self):
        return self.num1 % self.num2

    def floor_division(self):
        return self.num1 // self.num2
    
    def square_root(self):
        return self.num1 ** 0.5
    

c1 = Calculator(10, 2)

print(c1.add())
print(c1.subtract())
print(c1.multiply())
print(c1.divide())
print(c1.square())
print(c1.cube())
print(c1.power_of())
print(c1.mod())
print(c1.floor_division())
print(c1.square_root())