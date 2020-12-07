#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте рекурсивную функцию, печатающую все возможные перестановки для целых
# чисел от 1 до N.

import sys


def permutation(s):
    if len(s) == 1:
        return [s]

    perm_list = []
    for a in s:
        elements = [x for x in s if x != a]
        z = permutation(elements)

        for t in z:
            perm_list.append([a] + t)

    return perm_list


if __name__ == '__main__':
    n = int(input())

    arr = list(range(1, n + 1))

    for line in permutation(arr):
        print(line)