class People: #定义类，使用驼峰格式
    # 共有特征，叫做类属性
    head = 1 #类属性(类变量）

    def __init__(self,name,age,height): #固定形式 绝大多数情况下会使用__init__方法来创建属性
        #构造器
        self.fair = "假发"
        self.peoplename = name  #属性
        self.peopleage = age  #属性
        self.peopleheight = height  #属性
    def run(self):   #带self 往往把他叫做实例方法
        #self跟调用方法的对象ID一致
        #在方法中可以使用 self.属性 调用类属性
        print("{}是孩子，会跑！！！".format(self.peoplename)) #实列方法可以使用 self.属性名 调用属性值
    def sleep(self): #带self 往往把他叫做实例方法
        print("{}会睡觉！！".format(self.peoplename))

    def info(self):
        #在类里面，可以使用类名.类属性 来获取类属性值
        # print("类属性的值 {}".format(People.head))
        # 在类里面，可以使用self.类属性 来获取类属性值
        print("类属性的值 {}".format(self.head))

    def __str__(self): #魔术方法
        #如果使用print函数打印一个对象，那么会自动调用__str__实例方法
        #往往__str__实例方法，需要返回一个字符串
        return "<{}>".format(self.peoplename)
#可以使用类来创建多个对象
#每个对象之间，拥有不同的属性值
one_people = People("lemon",29,180)  #创建对象（这里one_people就是一个对象）----类名() 默认会调用__init__方法
two_people = People("哈喽",28,190)
# one_people.run() #使用对象.方法名 来调用方法
# one_people.sleep() #对象将自身自动传给了self
# two_people.run()
# print(one_people)
# print(two_people)
# print(one_people.fair)
# print(two_people.fair)
# print(one_people.six) #类属性可以使用 实列名调用
# print(People.six) #类属性可以使用 类名调用
#在类的外面访问类属性
#1.类名.类属性
# print(People.head)
# #2.对象.类属性
# print(one_people.head)
# print(two_people.head)

one_people.info()
# People.head = 2 #用类名.属性值 修改类属性，相当于修改了全局变量，后面所有对象调用的值是修改后的值（这个相当于类属性）
one_people.head = 2 #用对象名.属性值 修改类，相当于只修改了单个对象的类属性，其他对象调用值还是原来的值（这个相当于实例属性）
one_people.info()
two_people.info()
#类属性是所有对象共有的，实例属性的值是每个对象独有的

