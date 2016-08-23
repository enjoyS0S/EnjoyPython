#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:求 s = a + aa + aaa + aaaa + aaa...a的值其中a是一个数字。例如2 + 22 + 222 + 2222 + 22222(此时共有5个数相加),几个数相加有键盘控制

Tn = 0
Sn = 0
n = int(input('n = :\n'))
a = int(input('a = :\n'))

for count in range(n):
    Tn = Tn + a
    a *= 10
    Sn += Tn
    print(Tn)

print(Sn)
