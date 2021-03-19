print("Введите катеты треугольника:")
a = float(input("a = "))
b = float(input("b = "))
from math import sqrt
c = sqrt(a**2 + b**2)
p = a + b + c
print("Периметр треугольника: %.2f" % p)
print("Гипотенуза: %.2f" % c)
