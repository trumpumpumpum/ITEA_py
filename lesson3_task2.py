import functools
my_random_list_or_tuple = [1, 3, 3, 8]
print ("Сумма всех элементов : ",end="")
def function(a, b):
    return a + b
print (functools.reduce(function, my_random_list_or_tuple))