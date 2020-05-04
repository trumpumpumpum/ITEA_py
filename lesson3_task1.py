import random
N = int(input('Веедите количество значений списка: '))
x = []
for i in range(N):
    x.append(random.randint(0, N))
    # В random.randint вместо N можно было указать другой диапазон, но решил оставить N
even_list = [i for i in x if i % 2 == 0]
if even_list == []:
    print('Четных чисел в списке нет')
else:
    print(even_list)


