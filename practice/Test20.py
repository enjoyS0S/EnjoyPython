#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:一球从100米高度自由落下,每次落地后调回原高度的一般;再落下,求它在第10次落地时,共经过多少米?第10次反弹多高?

Sn = 100.0
Hn = Sn / 2

for n in range(2, 11):
    Sn += 2 * Hn
    Hn /= 2
print('Total of road is %f' % Sn)
print('The tenth is %f meter' % Hn)
