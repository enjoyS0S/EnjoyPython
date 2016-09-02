#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:一个五位数,判断是不是回文数。即12321是回文数,个位与万位相同,十位与
# 千位相同

a = int(input('Please input a number: \n'))
x = str(a)
flag = True

for i in range(int(len(x) / 2)):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print('%d 是一个回文数!' % a)
else:
    print('%d 不是一个回文数!' % a)

if x == x[::-1]:
    print('%d 还是一个回文数!' % a)
else:
    print('%d 还不是一个回文数!' % a)
