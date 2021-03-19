print("Введите 3 числа:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a > b :
    if a < c :
       s = a
       z = c
    elif c > b:
         s = c
         z = a
    elif b > c:
         s = b
         z = a

if b > a :
    if a > c :
       s = a
       z = b
    elif c < b:
         s = c
         z = b
    elif c > b:
         s = b
         z = c
         
print("Сумма двух наибольших = %.2f" % (z + s))
