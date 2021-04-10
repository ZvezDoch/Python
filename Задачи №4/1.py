a=1.08
print("Число a = ", a)
n=2
t=1+1/n
print("Числа, которые не меньше a:")
while t>a:
    print(t)
    n=n+1
    t=1+1/n
print("-----------------------")
