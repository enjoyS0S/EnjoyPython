#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:使用 lambda 来创建匿名函数


MAXIMIN = lambda x, y: (x > y) * y + (x < y) * y
MINIMUN = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('The larger one is %d' % MAXIMIN(a, b))
    print('The lower one is %d' % MINIMUN(a, b))
