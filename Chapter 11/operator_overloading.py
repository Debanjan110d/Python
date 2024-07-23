class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __str__(self):
        return str(self.n)

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n / other.n

    def __floordiv__(self, other):
        return self.n // other.n

    def __mod__(self, other):
        return self.n % other.n

    def __pow__(self, other):
        return self.n ** other.n

    def __lt__(self, other):
        return self.n < other.n

    def __gt__(self, other):
        return self.n > other.n

    def __eq__(self, other):
        return self.n == other.n

n = Number(1)
m = Number(2)
print(n == m)  # Corrected line
print(n + m)
print(n * m)
print(n / m)
print(n // m)
print(n % m)
print(n ** m)
print(n < m)
print(n > m)
print(n == m)
        