#-字符串：一串字符
#字符串 数字索引
# one_str = "my name is python"
# # print(one_str[3]) #索引为3的字符
# # print(type(one_str[2])) #查看类型
# #切片
# print(one_str[:]) #从头取到尾
# print(one_str[3:7]) #从第3位开始取（注意是从0开始的，只取到第6位）
# print(one_str[::2]) #从头到尾，每两位取一位
# #更新字符串
# print(one_str[:18] + '3') #在第18位加一个3
#字符串格式化
# name = input("请输入你的名字：")
# age = int(input("请输入你的年龄："))  #int将接收到的数据转换为int型（整数）
# print("你的名字是 {},你的年龄是 {:d}".format(name, age)) #format中的变量按照顺序传入到｛｝中，｛：d｝限制传入数据格式
# print("你的年龄是 {1}，你的名字是 {0}".format(name, age)) #｛｝中可以指定format传入顺序
#list
one_list = ['fangkun',100,None,'隔壁老方',['dog','haha',100]]
# print(one_list[0])
# print(one_list[0:3])
#插入一个元素
# one_list.insert(1,'太阳') #在第一位插入元素（在指定位置插入元素）
# print(one_list)
#在末尾追加数据
# one_list.append('活着')
# print(one_list)
two_list = ['python','java','c#']
one_list.extend(two_list)  #extend会把列表中的元素拆出来一个一个添加进去，append会将整个列表加进去
print(one_list)
#删除元素（pop）
# one_var = one_list.pop(0) #括号中可以指定删除位数
# print(one_list)
#清空列表（clear）
# one_list.clear()
# print(one_list)