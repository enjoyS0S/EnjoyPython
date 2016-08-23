#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 字符串日期转换为易读的日期格式
import time

# dt = parser.parse('Aug 18 2016 4:51PM')
ptime = time.strptime("Sat Aug 18 22:24:24 2016", "%a %b %d %H:%M:%S %Y")
print(ptime)
