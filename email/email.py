#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['442799812@qq.com']  # 接受邮件的地址

# 三个参数:第一个为文本内容,第二个 plain 设置文本格式,第三个 utf-8设置编码
message = MIMEText('Pythone 邮件发送测试', 'plain', 'utf-8')
message['From'] = Header('菜鸟教程', 'utf-8')
message['To'] = Header('测试', 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtplib = smtplib.SMTP('localhost')
    smtplib.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:发送失败')
