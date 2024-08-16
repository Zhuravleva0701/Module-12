import math


def test(*params, a=8):
    print('Привет, я тест', *params, a)


test(3, 5, 7, 9)

def test2(**params):
    print(params)

test2(Вася = 3, Женя = 8, Петя = 14)


def factorial(n):
    if n == 0 or n == 1:
        return 0 or 1
    else:
        return factorial(n-2)*(n-1) * n


print(factorial(6))


