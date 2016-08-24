#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:学习视同 auto 定义变量的用法
# 分析:没有 auto 关键字,使用变量作用于来举例说明

num = 2


def autofunc():
    num = 1
    print('Internal block num = %d' % num)
    num += 1


for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()
