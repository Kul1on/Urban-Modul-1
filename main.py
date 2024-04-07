

#Два предыдущих кода

def print_params(a=1, b='bruh', c=True):

    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'sad', False]
values_dict = {'a': 5, 'b': 'Who', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [4, 'good']
print_params(*values_list_2, 42)
def def_test(*args):
    for arg in args:
        print(arg)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def_test(1, 'bruh', [1, 2, 3], True)

print(factorial(6))


#Где я сейчас. Домашняя работа по уроку "Модули и пакеты"
import functions

functions.print_helloworld()
functions.print_helloworld()


