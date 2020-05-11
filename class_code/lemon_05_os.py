import os

# print(os.listdir(".")) #获取当前路径下所有文件，多加一个.是获取上级目录
#去掉文件名，返回目录
print(os.path.dirname('D:\www\lemon\class_code\lemon_01.py'))
#把目录和文件名合成一个路径
print(os.path.join('D:\www\lemon\class_code','lemon_01.py'))
#把路径分割成 dirname 和 basename，返回一个元组
print(os.path.split("D:\www\lemon\class_code\lemon_01.py"))
