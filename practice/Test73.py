#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:反向输出链表

if __name__ == '__main__':
    ptr = []
    n = int(input("Please input list length:\n"))
    for i in range(n):
        num = int(input('Please input a number:\n'))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)
