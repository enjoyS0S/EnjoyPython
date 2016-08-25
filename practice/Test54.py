#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:去一个整数 a 从右端开始的4-7位
# 分析:(1)先使 a 右移4位
#     (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
#     (3)将上面二者进行&运算


if __name__ == '__main__':
    a = int(input('Please input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print('%o\t%o' % (a, d))
