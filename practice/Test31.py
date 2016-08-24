#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:输入星期几的第一个字母来判断一下是星期几,如果第一个字母一样,则继续
# 输入第二个字母

letter = input('Please input: ')
# while letter != 'Y'
if letter == 'S':
    letter = input('Please input second letter,please input: ')
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('Data error')
elif letter == 'F':
    print('Friday')
elif letter == 'M':
    print('Monday')
elif letter == 'T':
    letter = input('Please input second letter,please input: ')
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('data error')
elif letter == 'W':
    print("Wednesday")
else:
    print('Data error')
