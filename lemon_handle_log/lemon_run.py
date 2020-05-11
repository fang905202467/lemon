import unittest
import HTMLTestReportCN
import time
from lemon_handle_config.handle_config import do_config

one_suite = unittest.defaultTestLoader.discover(".") #.代表当前py文件所在路径
test_reoprt = r'D:\www\lemon\report'

now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = test_reoprt + '\\' + now + do_config.get_config("report","report_name") + '.html'
fp = open(filename, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title=do_config.get_config("report","title"),
                                         description=do_config.get_config("report","description"),
                                         tester=do_config.get_config("report","tester"))
runner.run(one_suite)
fp.close()
