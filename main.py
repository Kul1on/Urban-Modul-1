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
