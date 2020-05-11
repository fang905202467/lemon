
class Animal:

    def __init__(self,name,colour,gender):
        self.name = name
        self.colour = colour
        self.genfer = gender
    def eat(self):
        print("{}会吃饭".format(self.name))
    def sleep(self):
        print("{}会睡觉".format(self.name))
    def call(self):
        print("{}会叫".format(self.name))

class Cat(Animal): #集成Animal类  Animal就是父类（基类） Cat就是子类

    def catching_mice(self):
        print("{}会捉老鼠\n颜色:{}\n性别:{}".format(self.name,self.colour,self.genfer))
class Dog(Animal):

    def wang_wang_barks(self):
        print("{}会汪汪叫\n颜色:{}\n性别:{}".format(self.name, self.colour, self.genfer))
class XiaoTianQuan(Dog):

    def __init__(self,name,colour,gender,job):
        #拓展，在父类的方法基础上，新增内容
        super().__init__(name,colour,gender) #继承父类方法
        self.job = job

    def wang_wang_barks(self):
        super().wang_wang_barks()
        print("工作:{}".format(self.job))

    def sleep(self):
        #对父类方法进行重写
        #如果定义了和父类相同的方法名，那么会将父类的方法覆盖掉
        print("{}是神仙，不会睡觉".format(self.name))

    def fly(self):
        print("{}会飞\n颜色:{}\n性别:{}\n工作：{}".format(self.name, self.colour, self.genfer,self.job))

xt = XiaoTianQuan("哮天犬","黑色","公","守护")
xt.fly()
xt.sleep() #对象可以调用父类的实例方法 这里sleep()就是父类Animal的实例方法
xt.wang_wang_barks()