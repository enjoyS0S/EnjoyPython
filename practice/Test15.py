#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:利用条件运算符的嵌套来完成此题:学习成绩>=90分的同学用A 表示,60-89分之间的用B表示;60分以下的用C表示。
# 程序分析:

score = int(input('input number:\n'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
print(grade)
