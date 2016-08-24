#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:求100之内的素数

lower = int(input('Input lower: '))
upper = int(input('Input upper: '))
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)
