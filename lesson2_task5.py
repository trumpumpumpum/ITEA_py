import functools
my_random_list = [3, 58, 11]
print ("Сумма всех элементов списка : ",end="")
def function(a, b):
    return a + b
print (functools.reduce(function, my_random_list))


