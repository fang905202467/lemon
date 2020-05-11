# -*- coding: UTF-8 -*-
# @Time : 2020/5/6 17:23 
# @Author : 隔壁老方
# @File : lemon_02_write_config.py
# @Software: PyCharm

from configparser import ConfigParser

#1.创建配置解析器对象
config = ConfigParser()

#2.构造要写入的数据
#嵌套字典的字典
datas = {
    "file_path":{
        "cases_path":"cases.xlsx",
        "log_path":"test_case.txt"
    },
    "msg":{
        "success_result":"Pass",
        "Fail_result":"Fail"
    }
}
for key in datas: #用for循环 把datas中的key值赋值给key，
    config[key] = datas[key] #datas[key]是datas中的字典数据 赋值给config[key]
#3.保存到文件
with open("write_config.ini","w") as file:
    config.write(file)