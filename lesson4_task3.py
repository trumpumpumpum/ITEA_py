from collections import Counter
my_list = (input('Введите последовательность: '))


def function (x):
    return x[1]

sublist, count = max(Counter(tuple(sorted(x)) for x in my_list).items(), key=function)
print('%s - %d' % (list(sublist), count))