from random import randint
from datetime import datetime

def my_decorator(func):
    def wrapper():
        time_start = datetime.now()
        result = func()
        return 'Время и дата вызова функции: ', time_start, '\n', result
    return wrapper


@my_decorator
def random_list():

    List = []
    for i in range(100000):
        List.append(randint(0, 1000))
    return 'Результат выполнения функции: ', List
file = open(r'C:\Users\Igor\PycharmProjects\untitled2\lesson6\logs.txt', 'a', encoding='utf-8')
for i in random_list():
    file.write(str(i))
file.close()






