class Jisuan:

    def __init__(self,one_num,two_num):
        self.one_num = one_num
        self.two_num = two_num

    def add(self):
        result = self.one_num + self.two_num
        return result

    def reduce(self):
        result = self.one_num - self.two_num
        return result

    def ride(self):
        result = self.one_num * self.two_num
        return result

    def excep(self):
        result = self.one_num / self.two_num
        return result
