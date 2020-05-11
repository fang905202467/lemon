# -*- coding: UTF-8 -*-
# @Time : 2020/5/9 15:34 
# @Author : fangkun
# @File : lemon_03_chaxun.py 
# @Software: PyCharm
#登录接口获取cookies 然后查询接口使用获取到的cookies请求
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
#这里登录后被重定向 只有添加（allow_redirects=False）才可以获取到登录后的cookies
login_res = requests.post(login_url,data=login_data,allow_redirects=False)
cookie = login_res.cookies
# print(cookie)
#查询请求
chaxun_res = requests.get(chaxun_url,params=chaxun_data,cookies=cookie)

# print(chaxun_res.text)
pass
# print(res.status_code)