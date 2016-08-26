#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymysql

db = pymysql.connect('localhost', 'root', 'test123', 'TESTDB')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version: %s' % data)
db.close()
