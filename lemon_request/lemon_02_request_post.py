# -*- coding: UTF-8 -*-
# @Time : 2020/5/9 14:40 
# @Author : fangkun
# @File : lemon_02_request_post.py 
# @Software: PyCharm

import requests
import json

#1.构造请求的url
url = "http://47.104.90.247:8000/api/add_event/"

#2.创建请求参数
params = {
        'eid':'10',
        'name':'宝马X15发布会',
        'limit':'10000',
        'status':'1',
        'address':'龙泉一区',
        'start_time':'2020-05-25 12:00:00'
}
#反爬虫措施，所以有时需要自己添加合法的请求，但是大多数情况下，不需要修改
headers = {
    "User-Agent": "Mozilla/5.0 gebilaofang"
}
#3.向服务器发起请求
#如果给params传参，那么传的参数数查询字符串参数
# res = requests.post(url,params=params,headers=headers)  #返回的是一个response对象，就可以把它当作是一个响应报文
#如果给data传参，那么会以x-www-form-urlencoded的形式来传参
res = requests.post(url,data=params,headers=headers)
#如果给json传参，那么会以json格式的字符串来传参
#所有的参数都转换为字典之后来传参
# res = requests.post(url,json=params,headers=headers)
pass
# #获取响应状态码
# print(res.status_code )
# print(res.text) #获取响应报文
# print(res.json()) #将响应报文转换为python中的数据类型
# print(res.cookies) #获取cookie
