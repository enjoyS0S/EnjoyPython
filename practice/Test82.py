#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:八进制转换为十进制

if __name__ == '__main__':
    n = 0
    p = input('Input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)
