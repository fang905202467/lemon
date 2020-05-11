# -*- coding: UTF-8 -*-
# @Time : 2020/5/9 16:29 
# @Author : fangkun
# @File : lemon_04_session.py 
# @Software: PyCharm
#创建Session会话对象来管理cookies，下面登录后再进行查询就不需要我们手动传入cookies了
import requests
#构造url
login_url = "http://47.104.90.247:8000/login_action/" #登录
chaxun_url = "http://47.104.90.247:8000/search_name/" #查询
#构造参数
login_data = {
    'username':'admin',
    'password':'admin123456'
}

chaxun_data = {
    'name':'11'
}
#登录请求
#1.创建Session会话对象
one_session = requests.Session() #Session会话对象，相当于Jmeter当中的Cookie管理器，会帮我们自动管理cookies
#2.使用Session会话对象的post来发起请求
login_res = one_session.post(login_url,data=login_data) #使用Session会话对象的post来请求，会帮我们管理cookies
#3.使用Session会话对象的get来发起请求
chaxun_res = one_session.get(chaxun_url,params=chaxun_data) #使用Session会话对象的get来请求，会帮我们传入cookies
#4.关闭会话
#关闭后，依然可以发起请求
#关闭会话只不过是释放资源
one_session.close()
