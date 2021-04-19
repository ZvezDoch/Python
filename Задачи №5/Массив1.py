a = [[3, 2, 5, -4], [8, 1, -1, 2], [1, 2, 3, 4], [1, -2, 3, 1]]

print("Изначальная матрица: ")      
for i in range(0, 4):
    for j in range(0, 4):
        print(a[i][j], end = " ")
    print()
    
s = [0]*4
print("Максимальные элементы в каждом столбце: ")      
for v in range(0, 4):
    for w in range(0, 4):
        if a[v][w] > s[w]:
            s[w] = a[v][w]

for d in range(0, 4):
    print(s[d], end = " ")


print("")
print("____________")

