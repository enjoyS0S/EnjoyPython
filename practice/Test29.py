#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:给一个不多于5位的正整数,要求:1、求它是几位数;2、逆序打印出各位数字。

x = int(input('Please input five-digit number: \n'))
a = int(x / 10000)
b = int(x % 10000 / 1000)
c = int(x % 1000 / 100)
d = int(x % 100 / 10)
e = int(x % 10)

if a != 0:
    print('five: ', e, d, c, b, a)
elif b != 0:
    print('four: ', d, c, b, a)
elif c != 0:
    print('three: ', c, b, a)
elif d != 0:
    print('two', b, a)
else:
    print('one', a)
