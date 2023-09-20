class ComplexNumber:
    def __init__(self, realPart, complexPart):
        self.realPart = realPart
        self.complexPart = complexPart

    def __add__(self, other):
        real = self.realPart + other.realPart
        complex = self.complexPart + other.complexPart
        return ComplexNumber(real, complex)

    def __sub__(self, other):
        real = self.realPart - other.realPart
        complex = self.complexPart - other.complexPart
        return ComplexNumber(real, complex)

    def __mul__(self, other):
        real = (self.realPart * other.realPart) - (self.complexPart * other.complexPart)
        complex = (self.realPart * other.complexPart) + (self.complexPart * other.realPart)
        return ComplexNumber(real, complex)

    def __str__(self):
        return f"{self.realPart} + {self.complexPart}i"

real_part1 = int(input("Enter the real part of the first complex number: "))
complex_part1 = int(input("Enter the complex part of the first complex number: "))
obj1 = ComplexNumber(real_part1, complex_part1)

real_part2 = int(input("Enter the real part of the second complex number: "))
complex_part2 = int(input("Enter the complex part of the second complex number: "))
obj2 = ComplexNumber(real_part2, complex_part2)

print("First Complex Number:", obj1)
print("Second Complex Number:", obj2)
print("Addition:", obj1 + obj2)
print("Subtraction:", obj1 - obj2)
print("Multiplication:", obj1 * obj2)
