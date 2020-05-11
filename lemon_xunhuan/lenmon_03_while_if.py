
day = ("周一","周二","周三","周四","周五","周末","周末")
while True:
    input_int =int(input("请输入数字1-7："))
    if input_int in (1,2,3,4,5,6,7):  #判断input_int 是否在 “1234567”中
        print("对应：{}".format(day[input_int - 1]))
    elif input_int == 0:
        print("程序退出！！")
        break
    else:
        print("输入错误，请重新输入!")