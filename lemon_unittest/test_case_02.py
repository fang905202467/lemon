import unittest
from lemon_unittest.csdemo import Jisuan
class Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        wenjian = "test_case.txt"
        cls.rizhi = open(wenjian,"a",encoding="utf8")
        cls.rizhi.write("\n{:=^40s}\n".format("测试用例开始执行"))

    @classmethod
    def tearDownClass(cls):
        cls.rizhi.write("{:=^40s}\n".format("测试用例执行结束"))
        cls.rizhi.close()

    def test_ride(self):
        try:
            actual_results = Jisuan(1,2).ride()
            expected_results = 2
            self.assertEqual(expected_results,actual_results)
            self.rizhi.write("test_ride:两数相加测试通过：PASS\n")
        except AssertionError as e:
            self.rizhi.write("test_ride:两数相加测试失败：FAIL-[{}]\n".format(e))
            raise e #因为上面捕获了异常，所以这里用raise来返回异常
    def test_excep(self):
        try:
            actual_results = Jisuan(1,2).excep()
            expected_results = -1
            self.assertEqual(expected_results,actual_results)
            self.rizhi.write("test_excep:两数相加测试通过：PASS\n")
        except AssertionError as e:
            self.rizhi.write("test_excep:两数相加测试失败：FAIL-[{}]\n".format(e))
            raise e #因为上面捕获了异常，所以这里用raise来返回异常

if __name__ == '__main__':
    unittest.main()