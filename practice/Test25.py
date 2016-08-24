#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:求1! + 2! + 3! + ... + 20!的和

# Method 1
s = 0
t = 1
for i in range(1, 21):
    t *= i
    s += t
print('1! + 2! + 3! + ... + 20! = %d' % s)

# Method 2
s = 0
l = range(1, 21)


def op(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r


s = sum(map(op, l))
print('1! + 2! + 3! + ... + 20! = %d' % s)
