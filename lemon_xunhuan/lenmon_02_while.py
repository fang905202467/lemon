#判断输入年份是否是闰年
year = int(input("请输入年份（如2020）:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #判断（year能否被4整除和不能被100整除）或者（year能否被400整除）
    print("{}是闰年！".format(year))
else:
    print("{}不是闰年！".format(year))