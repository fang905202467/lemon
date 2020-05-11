# -*- coding: UTF-8 -*-
# @Time : 2020/5/11 17:35
# @Author : fangkun
# @File : lemon_01_handle_mysql.py
# @Software: PyCharm

import pymysql

# 1.建立连接
conn = pymysql.connect(host='',
                user='',
                password='',
                db='',
                port='',
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
                )
#2.创建游标
cursor = conn.cursor()

#3.执行sql语句
sql = "select * from "
cursor.execute(sql)

conn.commit()

pass
