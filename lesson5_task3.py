from random import randint
import time
start_time = time.time()

List = []
for i in range(100000):
    List.append(randint(0, 1000))
print('Список случайных элементов: \n', List, '\nВремя выполнения: ', time.time() - start_time)


