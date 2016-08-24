#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 两个乒乓球队进行比赛,各出三人。甲队为 a,b,c 三人,乙队为 x,y,z 三人。已抽签决定比赛名单。有人向队员打听比赛名单。a 说他不和x ,c 和他不和 x,z 比。确定这比赛名单

for i in range(ord('c'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        if i != j:
            for k in range(ord('x'), ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print('order is a -- %s\t b -- %s\t c -- %s' % (chr(i), chr(j), chr(k)))
