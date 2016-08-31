#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:时间函数举例


if __name__ == '__main__':
    import time

    start = time.clock()
    for i in range(10000):
        print(i)
    end = time.clock()
    print('Different is %6.3f' % (end - start))
