#异常

# try:
#     int(input("请输入一个数字：")) #如果try中出现异常，直接执行except中的内容（不会管后面的内容）
#     print("这里执行吗")
# except:
#     print("cuowu")


#异常固定格式
# try:
#     num = int(input("请输入一个数字：")) #int处理用户输入的内容，如果输入数字之外的字符会报异常
#     result = (1/num)
#     print("会执行吗？？？") #上面有异常这里不会执行，没有异常才会执行
#     #如果除数为0会报异常
# except (ValueError,NameError): #可以多个异常类型放一起（要加括号），判断异常是否是其中一个
#     print("错误类型为：{}".format(ValueError))
# except ZeroDivisionError as e: #除数为0的异常
#     print('error = {}'.format(e))
# except Exception as result: #捕获所有类型异常
#     print(result)
# else: #没有异常才会执行
#     print('没有异常哦！！！')
# finally: #无论是否有异常，都会执行
#     print("无论是否有异常，都会执行")

#循环判断异常
while True:
    try:
        int(input("请输入一个数字：")) #如果用户不输入数字 就不会执行break 会一直循环
        break
    except Exception as result:
        print(result)
