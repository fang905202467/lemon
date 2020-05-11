
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
    def run(self):
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

    def __str__(self): #魔术方法
        #打印对象自动调用此函数
        #往往__str__方法，需要返回一个字符串
        return "对象是{}".format(self.name)

#创建对象（可以创建无数个对象）
one_people = HumanBeings("隔壁老方",26,"男") #这里会默认调用__init__方法（init中需要传入参数 括号中就需要参数传入）
two_people = HumanBeings("隔壁老王",28,"女")
#对象.方法 调用类中方法
one_people.run() #调用实例方法时，会将one_people传给run的形参self
two_people.run()
#类之外调用类属性
#1.类名.属性名
print(HumanBeings.head)
#2.对象名.属性名
print(one_people.head)
#打印对象
print(one_people)#这里会自动调用__str__方法
print(two_people)