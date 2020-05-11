# -*- coding: UTF-8 -*-
# @Time : 2020/5/11 17:35
# @Author : fangkun
# @File : lemon_01_handle_mysql.py
# @Software: PyCharm

import pymysql

# 1.建立连接
conn = pymysql.connect(host='47.104.90.247',
                       user='root',
                       password='fk@905202467',
                       db='guest',
                       port=3306,
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor   #这里指定dict游标类获取的数据是字典类型
                       )
# 2.创建游标
cursor = conn.cursor()

# 3.执行sql语句
# id = input("请输入要查询的ID:")
# sql_1 = "SELECT * FROM sign_event WHERE id=1"
sql_2 = "SELECT * FROM sign_event LIMIT 0,3"

# cursor.execute(sql_1)  # 执行sql
# cursor.execute(sql_1, args=(id,))  # args需要传一个序列类型，列表、元祖、字符串 这里id加个，表示元祖
cursor.execute(sql_2)
# 需要手动提交
conn.commit()
# 获取执行结果
# result1 = cursor.fetchone() #fetchone只返回一个结果，一条记录组成的字典
result2 = cursor.fetchall() #fetchall返回一组数据
pass
# 4.关闭连接(先关闭游标)
cursor.close()
conn.close()
