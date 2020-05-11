# -*- coding: UTF-8 -*-
# @Time : 2020/5/9 11:10 
# @Author : fangkun
# @File : lemon_01_json.py 
# @Software: PyCharm

import json
#json格式数据，key值必须用双引号，null是json中的格式，如果出现null可以直接判断就是json格式数据
one_json = '{"name":"隔壁老方","age":"26","money":null,"love":"True"}' #在python中json是以字符串格式来呈现，所以要加单引号

#json格式数据转换为字典
one_dict = json.loads(one_json,encoding="utf-8") #转换后json中的null会转换成python中的None

#dict类型数据转换为json
#indent=2 显示格式缩进2个空格显示
two_json = json.dumps(one_dict,ensure_ascii=False,indent=2) #ensure_ascii=False 表示不用编码，中文就会正常显示
print(two_json)




