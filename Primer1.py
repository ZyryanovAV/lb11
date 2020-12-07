# -*- coding: utf-8 -*-
# Рекурсивная версия

import timeit


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    r_fib = fib(30)
    r_factorial = factorial(30)

    print(timeit.timeit("r_factorial", setup="from __main__ import r_factorial"))
    print(timeit.timeit("r_fib", setup="from __main__ import r_fib"))
