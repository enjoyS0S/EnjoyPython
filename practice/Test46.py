#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:求输入数字的平方,如果平方运算后小于50则退出

TRUE = 1
FALSE = 0


def SQ(x):
    return x * x


if __name__ == '__main__':
    again = 1
    while again:
        num = int(input('Please input a number:\n'))
        print('运算的结果为:%d' % SQ(num))
        if num >= 50:
            again = TRUE
        else:
            again = FALSE
