my_string = input('Введите строку: ')
x = len(my_string)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if my_string[x - i] == my_string[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print('Не палиндром')
else:
  print('Палиндром')