import time

yue = 2000000
def login():
    '''
    登录函数
    :return:
    '''
    while True:
        password = input("请输入银行卡密码:")
        if password == '123456':
            print("密码正确，正在进入银行系统....")
            break
        else:
            print("密码错误，请重新输入。。。")


def shouye():
    time.sleep(3)
    print("---------------银行系统---------------")
    print("请选择服务项目：")
    print("1.余额查询\t", "2.取款\t", "3.转账\t", "4.存款\t", "5.修改密码")
    print("--------------------------------------")

#银行服务操作
def operation():
    '''
    银行服务操作函数
    :return:
    '''
    while True:
        caozuo = int(input("请输入服务号（0-5）:"))
        if caozuo == 1:
            print("---------------银行系统---------------")
            print("当前余额为 {}".format(yue))
            print("--------------------------------------")
            shouye()
        elif caozuo == 2:
            while True:
                print("---------------银行系统---------------")
                qkje = int(input("请输入取款金额:"))
                if qkje <= yue:
                    print("稍等！正在出钞中...")
                    time.sleep(2)
                    print("取款成功！！！")
                    shouye()
                    break
                else:
                    print("取款金额大于当前余额！请重新输入...")
        elif caozuo == 3:
            print("---------------银行系统---------------")
            zzzh = int(input("请输入转账账户:"))
            while True:
                zzje = int(input("请输入转账金额:"))
                if zzje <= yue:
                    print("转账成功！！")
                    shouye()
                    break
                else:
                    print("转账金额大于当前余额！请重新输入...")

login()
shouye()
operation()
