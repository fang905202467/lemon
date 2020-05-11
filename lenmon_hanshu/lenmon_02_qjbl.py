num_a = 500

def quanju():
    '''
    全局变量修改
    :return:
    '''
    global num_a #使用global定义全局变量
    num_a = 400
    print("内部变量：{}".format(num_a))

print("外部变量：{}".format(num_a))
quanju()