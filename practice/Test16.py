#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目:输出指定格式的日期

import datetime

if __name__ == '__main__':
    # 输出今日日期,格式为 dd/mm/yyyy
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(2016, 8, 23)
    print(miyazakiBirthDate.strftime('%y/%m/%Y'))

    # 日期算数运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstDirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
    print(miyazakiFirstDirthday.strftime('%d/%m/%Y'))
