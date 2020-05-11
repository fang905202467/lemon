import os

print(os.name) #获取当前计算机名字
print(os.getcwd()) #获取当前路径
print(os.mkdir("test")) #在当前目录创建文件夹
os.rmdir(r"D:\www\lemon\lenmon_hanshu\test") #删除目录test（这里用的绝对路径，r可以让转意符失效（比如\t））