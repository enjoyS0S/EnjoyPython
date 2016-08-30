#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:有n个整数,使其前面各数顺序向后移 m 个位置,最后 m 个数变成最前面的 m 个数


if __name__ == '__main__':
    n = int(input('The total number is:\n'))
    m = int(input('Back m:\n'))


    def move(array, n, m):
        array_end = array[n - 1]
        for i in range(n - 1, -1, -1):
            array[i] = array[i - 1]
        array[0] = array_end
        m -= 1
        if m > 0:
            move(array, n, m);


    number = []
    for i in range(n):
        number.append(int(input('Input a number:\n')))
    print('Orignal number:', number)
    move(number, n, m)
    print('After moved:', number)
