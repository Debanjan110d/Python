class Complex:
    def __init__(self,real,imag) :
        self.real = real
        self.imag = imag
        
    def _add_(self,c2):
        return Complex(self.real + c2.real, self.imag + c2.imag)
    
    def _sub_(self,c2):
        return Complex(self.real - c2.real, self.imag - c2.imag)

    def _mul_(self,c2):
        return Complex(self.real * c2.real - self.imag * c2.imag, self.real * c2.imag + self.imag * c2.real)

    def _str_(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2,3)
c2 = Complex(4,5)
c3 = c1._add_(c2)
print(c3._str_())
c4 = c1._sub_(c2)
print(c4._str_())
c5 = c1._mul_(c2)
print(c5._str_) 
