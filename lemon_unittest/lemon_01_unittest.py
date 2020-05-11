import unittest
from lemon_unittest.csdemo import Jisuan
class Test(unittest.TestCase):

    def test_01(self):
        result = Jisuan(1,2).add()
        self.assertEqual(result,3)
    def test_02(self):
        result = Jisuan(1,2).reduce()
        self.assertEqual(result,-1)
    def test_03(self):
        result = Jisuan(1,2).ride
        self.assertEqual(result,3)
    def test_04(self):
        yuqi = 2
        result = Jisuan(6,3).excep()
        self.assertEqual(yuqi,result,msg="两数相除测试失败")

if __name__ == '__main__':
    unittest.main()