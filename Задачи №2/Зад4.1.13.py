print("Введите 3 числа:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a > b :
    if a < c :
       s = a
    elif c > b:
         s = c
    elif b > c:
         s = b

if b > a :
    if a > c :
       s = a
    elif c < b:
         s = c
    elif c > b:
         s = b
print("Среднее число равно = %.2f" % s)
