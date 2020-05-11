# -*- coding: UTF-8 -*-
# @Time : 2020/5/6 16:04
# @Author : 隔壁老方
# @File : lemon_01_parser_config.py 
# @Software: PyCharm

#以.conf或者.ini 为拓展名的文件叫配置文件
#配置文件组成：
# 区域名
#选项名 = 选项值
from configparser import ConfigParser

#1.创建配置解析器对象
config = ConfigParser()

#2.指定读取的配置文件
config.read("config.conf",encoding="utf-8")

#3.读取数据
# one_value = config["file path"]["cases_path"]
#
# print("用例文件名为 {}\n类型为{}".format(one_value,type(one_value)))
# #读取数据第二种方法
# two_value = config.get('msg','success_result')
# print("用例文件名为 {}\n类型为{}".format(two_value,type(two_value)))
#从配置文件中，使用使用方括号或者get读取的值全部是str（字符串）类型

# dict = dict(config["file path"]) #可以用字典进行转换，转换后选项名是key，选项值是value
# print(dict)
#可以使用getint获取int类型的数据
# config.getint('msg','value')
#可以使用getfloat获取float类型的数据
# config.getfloat('msg','value2')
#可以使用getboolean获取bool类型的数据
#1、yes、on、true、True--->都会读取为True
#0、on、off、false、False-->都会读取为False
# one_bool = config.getboolean('msg','value4')
# print("用例文件名为 {}\n类型为{}".format(one_bool,type(one_bool)))

#eval函数能够将字符串转换为python中内置类型
#eval也能够执行字符串类型表达式
#相当于把字符串的引号去掉之后的类型
# one_list = config.get('msg', 'value7')
# one_list = eval(one_list) #这里eval将数据转换为list类型
# print("用例文件名为 {}\n类型为{}".format(one_list,type(one_list)))

#eval举例,最开始的值为字符串类型，通过eval转换后为元组类型
one_value = '(10,20)'
print(f"one_value的值为：{one_value}\n类型为:{type(one_value)}")
one_value = eval(one_value)
print(f"one_value的值为：{one_value}\n类型为:{type(one_value)}")

pass