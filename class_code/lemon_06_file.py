#操作文件
#必须的三个步骤
#1.打开文件
one_file = open("test.txt",encoding="utf8")
#2.读写文件
# re_file = one_file.read() #读取文件中所有内容
# re_file1 = one_file.readline() #读取文件中一行内容，第一个是读取第一行
# print(re_file1)
# re_file2 = one_file.readline()#读取文件中一行内容，第一个是读取第二行
# print(re_file2)
# re_file = one_file.readlines() #读取文件所有内容，以列表格式输出
# print(re_file)
for i in one_file.readlines(): #循环输出文件内容（一行一行的循环）
    print(i)
#3.关闭文件
one_file.close()