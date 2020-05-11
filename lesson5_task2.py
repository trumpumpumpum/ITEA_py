import time
time = time.localtime()
data = str(input('Введите данные с клавиатуры: '))
def input (a, b):
    return ('\nВремя Ввода: ', a, '\nТекст Который Ввел Пользователь: ', b)

file = open(r'C:\Users\Igor\PycharmProjects\untitled2\lesson5\user_data.txt', 'a', encoding='utf-8')
for i in input(time, data):
    file.write(str(i))
file.close()

