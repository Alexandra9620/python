class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


n1 = ComplexNumber(1, 2)
n2 = ComplexNumber(3, 4)

print(n1 + n2)
print(n1 * n2)
