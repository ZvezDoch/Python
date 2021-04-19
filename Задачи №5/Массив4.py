s = int(input("Введите размер массивa: "))
a = [0]*s

print("Введите элементы массива: ")
for i in range(0, s):
    a[i] = int(input())

for j in range(0, len(a)):
    if a[j] < 0:
        a.insert(j+1, 0)
        j = j+1
        
print("Новый массив: ")      
for d in range(0, len(a)):
    print(a[d], end = " ")
