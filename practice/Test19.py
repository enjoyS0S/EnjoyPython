#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:一个数如果恰好等于它的因子之和,这个数就称为"完数"。例如6 = 1 + 2 + 3.找出1000以内的所有的完数

from sys import stdout

for i in range(2, 1001):
    k = []
    n = -1
    s = i
    for j in range(1, i):
        if i % j == 0:
            n += 1
            s -= j
            k.append(j)
    if s == 0:
        print(i)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print(k[n])
