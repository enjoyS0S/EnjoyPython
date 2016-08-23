#!/usr/bin/python
# -*- coding: UTF-8 -*-

inputs = input('Please input a string:\n')
inputs = inputs.upper()
fp = open('text98.txt', 'w')
fp.write(inputs)
fp = open('text98.txt', 'r')
print(fp.read())
fp.close()
