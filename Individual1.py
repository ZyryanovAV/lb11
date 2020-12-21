#!/usr/bin/env 2.
# -*- config: utf-8 -*-

# Вариант 1. Напишите рекурсивную функцию, проверяющую правильность расстановки скобок в строке.
# При правильной расстановке выполняются условия:
# количество открывающих и закрывающих скобок равно.
# внутри любой пары открывающая – соответствующая закрывающая скобка, скобки
# расставлены правильно
 

def par_checker(simvol_string):
    new_list = []
    balanced = True
    index = 0

    while index < len(simvol_string) and balanced:
        simvol = simvol_string[index]
        if simvol in "(":
            new_list.append(simvol)
    else:
        if len(new_list) == 0:
            balanced = False
        else:
            top = new_list.pop()
            if not matches(top, simvol):
                balanced = False
        index += 1

    return balanced and len(new_list) == 0


def matches(open, close):
    opens = "("
    closers = ")"
    return opens.index(open) == closers.index(close)


if __name__ == '__main__':

    print(par_checker('((())())'))
    print(par_checker(')()'))