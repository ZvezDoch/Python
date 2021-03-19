print("Введите x:")
x = float(input("x = "))

if x > 0:
     from math import sin
     f = 2*sin(x)
     print("F(x) = 2*sin(x) = %.2f" % f)

if x <=  0 :
    g = 6 - x
    print("F(x) = 6 - x = %.2f" % g)

