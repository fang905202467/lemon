# -*- coding: UTF-8 -*-
# @Time : 2020/5/7 14:56 
# @Author : fangkun
# @File : lemon_01_handle_log_define.py 
# @Software: PyCharm

import logging #python内置的日志模块

#1.定义日志收集器
case_logger= logging.getLogger("case") #创建一个logger对象

#2.指定日志收集器的日志等级
#NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
case_logger.setLevel(logging.DEBUG) #只能手机当前等级和当前等级以上的级别日志
# case_logger.setLevel("DEBUG")

#3.定义日志输出渠道
#输出到控制台
console_handle = logging.StreamHandler() #handler对象
#输出到文件
file_handle = logging.FileHandler("cases.log", encoding="utf-8")

#4.指定日志输出渠道的日志等级
console_handle.setLevel(logging.ERROR)
file_handle.setLevel(logging.INFO)

#5.定义日志显示格式
simple_formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - [msg]: %(message)s')
verbose_formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(lineno)d - [msg]: %(message)s ')

console_handle.setFormatter(simple_formatter) #控制台使用定义的日志格式
file_handle.setFormatter(verbose_formatter) #文件使用定义的日志格式

#6.将日志收集器与输出渠道进行对接
case_logger.addHandler(console_handle)
case_logger.addHandler(file_handle)

if __name__ == '__main__':
    case_logger.debug("这是一个debug级别日志") #手动记录日志
    case_logger.info("这是一个info级别日志")
    case_logger.warning("这是一个warning级别日志")
    case_logger.error("这是一个error级别日志")
    case_logger.critical("这是一个critical级别日志")

