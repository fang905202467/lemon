# -*- coding: UTF-8 -*-
# @Time : 2020/5/9 11:42 
# @Author : fangkun
# @File : lemon_02_json_file.py 
# @Software: PyCharm

import json
#使用load()将文件中的json格式数据转换为字典
with open("file_json.txt",encoding="utf-8") as file:
    one_json = json.load(file)

print(f"数据为:{one_json}\n类型为：{type(one_json)}")

#使用()将文件中的json格式数据转换为字典
two_dict = [{"one": {"name":"隔壁老方","age":"26","money":None,"love":"True"}},
            {"two": {"name": "隔壁老三", "age": "27", "money": None, "love": "True"}}]
with open("write_json.txt","w",encoding="utf-8") as file:
    json.dump(two_dict,file,ensure_ascii=False,indent=2)