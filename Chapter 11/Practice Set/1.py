class TwoVector:
    def __init__(self, x, y):
        if x is None or y is None:
            raise ValueError("Both x and y coordinates must be provided")
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

class ThreeVector(TwoVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        if z is None:
            raise ValueError("z coordinate must be provided")
        self.z = z

    def show(self):
        super().show()
        print(self.z)

a = TwoVector(1, 2)
b = ThreeVector(1, 2, 3)