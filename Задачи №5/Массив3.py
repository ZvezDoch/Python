s = int(input("Введите размер массивов: "))
a = [0]*s
b = [0]*s
c = [0]*s

print("Введите элементы первого массива: ")
for i in range(0, s):
    a[i] = int(input())

print("Введите элементы второго массива: ")
for j in range(0, s):
    b[j] = int(input())
    
for f in range(0, s):
    if a[f] > b[f]:
        c[f] = a[f]
    else:
        c[f] = b[f]
        
print("Новый массив: ")      
for d in range(0, s):
    print(c[d], end = " ")


print("")
print("____________")
