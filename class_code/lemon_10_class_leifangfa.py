
class HumanBeings:
    '''
    人类
    '''
    head = 1 #类属性
    def __init__(self,name,age,six):
        #构造器（构造方法）
        #创建实例属性
        self.name = name
        self.age = age
        self.six = six
    def run(self): #实例方法
        #实例方法中调用属性 1.对象.属性名
        print("{} 会跑，年龄{}, 性别{}.".format(one_people.name,one_people.age,one_people.six))
        # 实例方法中调用属性 1.self.属性名
        print("{} 会跑".format(self.name))
        #实例方法中调用类属性 1.对象.属性名
        print("类属性是{}".format(one_people.head))
        # 实例方法中调用类属性 1.self.属性名
        print("类属性是{}".format(self.head))

    def eat(self):
        print("会吃饭")

    @classmethod  #构造器 说明这是这个类方法
    def sing(cls): #类方法只能调用和修改类属性
        print("{}个头".format(cls.head)) #调用类属性
        cls.head = 2 #修改类属性
        print("{}个头".format(cls.head))

    @staticmethod
    def tianqi(): #静态方法
        print("天气真好{}ge".format(HumanBeings.head)) #可以调用类属性


    def __str__(self): #魔术方法
        #打印对象自动调用此函数
        #往往__str__方法，需要返回一个字符串
        return "对象是{}".format(self.name)

#创建对象（可以创建无数个对象）
one_people = HumanBeings("隔壁老方",26,"男") #这里会默认调用__init__方法（init中需要传入参数 括号中就需要参数传入）
two_people = HumanBeings("隔壁老王",28,"女")

#调用类方法
# HumanBeings.sing() #调用类方法 会将类传给CLS
# one_people.sing()#调用类方法 会将类传给CLS
#调用静态方法
HumanBeings.tianqi()
one_people.tianqi()