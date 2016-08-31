#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:809*??=800*??+9*??+1其中??代表的两位数,8*??的结果为两位
# 数,9*??的结果为3位数。求??代表的两位数,及809*??后的结果。


a = 809
for i in range(10, 100):
    b = a * i + 1
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print(i)
        break
