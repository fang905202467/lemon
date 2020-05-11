# def add(one_num,two_num): #括号中是形参
#     '''
#     两个数相加
#     :param one_num:
#     :param two_num:
#     :return:
#     '''
#     result = one_num + two_num
#     print("{} + {} = {}".format(one_num,two_num,result))
#
# add(12,12) #括号中是实参（位置参数）

# max_num = 50 #函数外（全局变量）
# def hanshu():
#     max_num = 40 #局部变量
#     print(max_num)
# print(max_num)
# hanshu() #函数会先在内部找是否有变量，内部没有再找全局变量

#位置参数和关键字参数
# def test_hanshu(name,age,six):
#     print("name : {} ,age : {} ,six : {}".format(name,age,six))
#
# # test_hanshu("fangkun",28,"男") #位置参数（安装对应位置来传值，顺序不能乱）
# test_hanshu(name="haha",age=89,six="nan") #关键字参数（顺序可以乱）

#可变参数
# def variable(*args): #单个*号，参数以元组形式传入
#     '''
#     可变参数：可以将任意个数参数以元组形式传入到函数中
#     :param args:
#     :return:
#     '''
#     print("i = {} ,类型为：{}".format(args,type(args)))
# variable(1,"fangkun",89,None) #不限制个数

#可变参数两个*号
# def var(**kwargs):
#     '''
#     可变参数：可以将任意个数参数以字典形式传入到函数中
#     :param kwargs:
#     :return:
#     '''
#     print("i = {} ,类型为：{}".format(kwargs, type(kwargs)))
# var(a="fangk",b=12,c=123,d=True) #传入参数要是字典格式

#默认参数
def vaaa(name="kun",age=18,): #默认参数
    '''
    默认参数
    :param name:
    :param age:
    :return:
    '''
    print(name,age)
vaaa() #有默认参数 这里可以不传参数
vaaa('fang') #可以传入位置参数，会覆盖默认参数（这里把默认参数name的值改了）
vaaa(age=26) #可以传入关键字参数，也会覆盖默认参数（这里把默认参数age的值修改了）