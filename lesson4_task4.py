from random import randint
N = randint(0, 9)
M = randint(0, 9)
L = [[i * j for i in range(0, N)] for j in range(0, M)]
print('Список: \n', L)
S = 0
for i in range(len(L)):
     for j in range(len(L[i])):
         S += L[i][j]
     print('Cумма: ', S)
