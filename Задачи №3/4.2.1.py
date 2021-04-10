import random

N = random.randrange(10)+1
K = random.randrange(-10, 10)

print('K = ', K)
print('N = ', N)
for i in range(0, N):
    print(i+1," : ",K)
    
