#!/usr/bin/python
# -*- coding: UTF-8 -*-

fp = open('text1.txt')
a = fp.read()
fp.close()

fp = open('text1.txt')
b = fp.read()
fp.close()

fp = open('text3.txt', 'w')
l = list(a + b)
l.sort()
s = ''
s = s.join(l)
fp.write(s)
fp.close()
