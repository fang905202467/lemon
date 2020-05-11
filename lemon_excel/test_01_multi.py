#使用ddt来进行数据驱动
#根据用例的数量来自动生成实例方法，批量执行用例
import unittest
from lemon_excel.ddt import ddt, data
from lemon_excel.csdemo import Jisuan
from lemon_excel.lemon_03_handleexcel import HandleExcel

do_excel = HandleExcel("cases.xlsx","ride")
cases = do_excel.get_cases()
@ddt
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

    @data(*cases) #拆包   这里相当于for循环 每拆一次是一个元组会赋值给one_case
    def test_ride(self,one_case):
        actual_results = Jisuan(one_case['l_data'], one_case['r_data']).ride()
        msg = one_case['title']
        expected_results = one_case['expected']
        try:
            self.assertEqual(expected_results,actual_results, msg=msg)
            self.rizhi.write("test_ride:{} ,测试结果为 {}\n".format(msg,'Pass'))
            do_excel.write_result(one_case['case_id']+1,actual_results,"Pass")
        except AssertionError as e:
            self.rizhi.write("test_ride:{} ,测试结果为 {}.具体异常为{}\n".format(msg,'Fail',e))
            do_excel.write_result(one_case['case_id'] + 1, actual_results, "Fail")
            raise e #因为上面捕获了异常，所以这里用raise来返回异常

if __name__ == '__main__':
    unittest.main()
    #执行了多少条用例，用例条数与data装饰器的（位置）参数个数一致
    #ddt和data是黄金搭档，要一起使用才行