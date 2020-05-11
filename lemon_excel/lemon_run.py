import unittest
import HTMLTestReportCN
import time

one_suite = unittest.defaultTestLoader.discover(".") #.代表当前py文件所在路径
test_reoprt = r'D:\www\lemon\report'

now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = test_reoprt + '\\' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title='xx项目测试报告', description='用例执行情况：',tester="隔壁老方")
runner.run(one_suite)
fp.close()
