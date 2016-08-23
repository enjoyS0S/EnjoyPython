#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 从键盘输入一些字符，逐个把它们送到磁盘上去，直到输入一个#为止

file_name = 'text97.txt'
fp = open(file_name, 'w')
ch = input('Please input a string :')
while ch != '#':
    fp.write(ch)
    ch = input('')
fp = open(file_name, 'r')
print(fp.read())
