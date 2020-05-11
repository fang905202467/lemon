#拆包
# one_list = ["方坤","26","男"]
# name, age, six = one_list
# print(name,end="\t")
# print(age)
# print(six)
two_dict = {"name":"fangkun","age":"26","six":"nan"}
name, age, six = two_dict.items() #键值对一起拆包
print(name,end="\t")
print(age)
print(six)