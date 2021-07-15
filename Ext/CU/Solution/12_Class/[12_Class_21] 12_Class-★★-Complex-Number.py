class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imaginary = b

    def __str__(self):
        n = ''
        if self.real != 0:
            n += str(self.real)
        if self.imaginary == 1:
            n += '+i'
        elif self.imaginary == -1:
            n += '-i'
        elif self.imaginary > 0:
            n += '+'+str(self.imaginary)+'i'
        elif self.imaginary < 0:
            n += str(self.imaginary)+'i'
        if self.real == 0 and self.imaginary > 0:
            n = n[1:]
        if n == '':
            n = '0'
        return n

    def __add__(self, rhs):
        return Complex(self.real + rhs.real, self.imaginary + rhs.imaginary)

    def __mul__(self, rhs):
        a = self.real
        b = self.imaginary
        c = rhs.real
        d = rhs.imaginary
        R = (a * c) - (b * d)
        Im = (a * d) + (b * c)
        return Complex(R, Im)

    def __truediv__(self, rhs):
        a = self.real
        b = self.imaginary
        c = rhs.real
        d = rhs.imaginary
        k = c**2 + d**2
        R = (a * c) + (b * d)
        Im = - (a * d) + (b * c)
        return Complex(R/k, Im/k)


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1+c2)
elif t == 4:
    print(c1*c2)
else:
    print(c1/c2)
