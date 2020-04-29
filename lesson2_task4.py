length = float(input('Введите число в метрах: '))
measure = str(input('Выберите меру длины (mm, cm, km): '))
mm = 1000 * length
cm = 100 * length
km = 0.001 * length
if measure == 'mm':
    print(mm, 'mm')
elif measure == 'cm':
    print(cm, 'cm')
elif measure == 'km':
    print(km, 'km')
    