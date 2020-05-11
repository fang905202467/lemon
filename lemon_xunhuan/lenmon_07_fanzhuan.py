one_list = [48,3,100,8,9]
#翻转列表数据
two_list = []
for i in range(len(one_list)-1,-1,-1):  #最后一个-1表示从列表最后一位倒序取值
    two_list.append(one_list[i])
print(two_list)
#取出列表中最大值
max_data = 0
for i in one_list:
    if max_data < i:
        max_data = i
print("最大值为{}".format(max_data))
#方法2
print("最大值为{}".format(max(one_list)))
#排序取最大值
print(sorted(one_list)[-1])
