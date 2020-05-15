from random import randint

List = []
for i in range(100000):
     List.append(randint(0, 1000))

#Проверочный список: List = [4, 64, 16, 25, 81, 49]


def get_sq_root_list():
    return List
result = map(lambda number: number ** 0.5, get_sq_root_list())
print('Входная последовательность: \n', List, '\nПосле поиска корней: \n', tuple(result))

def median(l):
    n = len(l)
    if n < 1:
        return None
    elif n % 2 == 1:
        return sorted(l) [n // 2]
    else:
        return sum(sorted(l) [n // 2 - 1 : n // 2 + 1]) / 2.0

print('Медиана: ', median(List))

def is_greater_than_median(number):
    return number > median(List)
result = filter(is_greater_than_median, List)
print('Результат: \n', list(result))





