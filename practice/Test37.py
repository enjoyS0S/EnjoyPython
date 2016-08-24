#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:排序


if __name__ == '__main__':
    N = 10
    print('Please input ten number:\n')
    l = []
    for i in range(N):
        l.append(int(input('input number:\n')))
    print()
    for i in range(N):
        print(l[i])
    print()

    # sort ten number
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if l[min] > l[j]:
                min = j
        l[i], l[min] = l[min], l[i]
    print('after sorted')
    for i in range(N):
        print(l[i])
