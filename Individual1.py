#!/usr/bin/env 2.
# -*- config: utf-8 -*-

# Вариант 1. Напишите рекурсивную функцию, проверяющую правильность расстановки скобок в строке.
# При правильной расстановке выполняются условия:
# количество открывающих и закрывающих скобок равно.
# внутри любой пары открывающая – соответствующая закрывающая скобка, скобки
# расставлены правильно
 

def par_checker(symbol_string):
    s = []
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "(":
            s.append(symbol)
    else:
        if len(s) == 0:
            balanced = False
        else:
            top = s.pop()
            if not matches(top, symbol):
                balanced = False
        index += 1

    return balanced and len(s) == 0


def matches(open, close):
    opens = "("
    closers = ")"
    return opens.index(open) == closers.index(close)


if __name__ == '__main__':

    print(par_checker('((())())'))
    print(par_checker(')()'))