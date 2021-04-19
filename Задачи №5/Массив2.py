a = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

print("Изначальная матрица: ")      
for i in range(0, 4):
    for j in range(0, 4):
        print(a[i][j], end = " ")
    print()
    
m = int(input("Какой столбец нужно удалить?"))

print("Новая матрица: ")      
for i in range(0, 4):
    for j in range(0, 4):
        if j != m-1:
            print(a[i][j], end = " ")
    print()
