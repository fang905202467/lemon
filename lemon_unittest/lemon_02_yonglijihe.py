import unittest
from lemon_unittest import test_case_01
from lemon_unittest import test_case_02

#————————————第一种方法加载模块来加载用例——————————————————
#1.创建测试套件
one_suite = unittest.TestSuite()
#2.通过模块来批量加载测试用例
#先定义测试加载器对象
one_loader = unittest.TestLoader()
one_suite.addTest(one_loader.loadTestsFromModule(test_case_01)) #这里用加载器加载测试用例模块，然后放到套件当中
one_suite.addTest(one_loader.loadTestsFromModule(test_case_02))
#3.执行用例
#创建执行器
one_runner = unittest.TextTestRunner()
one_runner.run(one_suite)