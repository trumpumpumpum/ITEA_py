def two_num (a, b):
    if a == b:
        return True
    elif a - b == 5:
        return True
    elif b - a == 5:
        return True
    elif a + b == 5:
        return True
    else: return False


first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
# Можно было просто присвоить значения переменным first_num и second_num, но решил дать возможность ввода.
# Надеюсь, это не противоречит заданию
x = two_num (first_num, second_num)
print(x)



