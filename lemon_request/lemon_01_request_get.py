# -*- coding: UTF-8 -*-
# @Time : 2020/5/9 14:06 
# @Author : fangkun
# @File : lemon_01_request_get.py 
# @Software: PyCharm

import requests

#1.构造请求的url
url = "http://47.104.90.247:8000/api/get_event_list/"

#2.创建请求参数
params = {
    "eid":"1"
}

headers = {
    "User-Agent": "Mozilla/5.0 gebilaofang"
}
#3.向服务器发起请求
#如果给params传参，那么传的参数数查询字符串参数
res = requests.get(url,params=params,headers=headers)  #返回的是一个response对象，就可以把它当作是一个响应报文
#获取响应状态码
print(res.status_code )
print(res.text) #获取响应报文
print(res.json()) #将响应报文转换为python中的数据类型
print(res.cookies) #获取cookie
