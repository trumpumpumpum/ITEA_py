import random
num_try = 0
start_range = 0
end_range = 100
a = random.randint(0, 100)
while num_try < 4:
    user_number = int(input('Угадайте случайное число от 0 до 100: '))
    num_try += 1
    if user_number == a:
        print('Поздравляем, Вы ввели верное число!', 'Количество попыток:', num_try)
        break
    elif user_number < a and start_range <= user_number <= end_range:
        print('К сожалению, Вы не угадали. Число должно быть больше.', 'Количество попыток:', 4 - num_try)
    elif user_number > a and start_range <= user_number <= end_range:
        print('К сожалению, Вы не угадали. Число должно быть меньше.', 'Количество попыток:', 4 - num_try)

    # Числа, которые не входят в диапазон от 0 до 100 не учитывал, так как это не требовалось в задании.
    # Если учесть диапазон от 0 до 100 и тратить попытки на числа вне диапазона, то можно добавить:
    #else:
    #    print('Число не входит в диапазон от 0 до 100', 'Количество попыток:', 4 - num_try)



