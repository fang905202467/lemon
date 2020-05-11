import unittest
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner_Chart
from lemon_unittest import HTMLTestReportCN
from lemon_unittest import HTMLTestReportEN
from lemon_unittest import test_case_01
from lemon_unittest import test_case_02
import time

#—————————第二种方法加载当前路径（或者指定路径）下test_开头的py文件来加载用例———————————

one_suite = unittest.defaultTestLoader.discover(".") #.代表当前py文件所在路径
#创建执行器对象
# one_runner = unittest.TextTestRunner()
# one_runner.run(one_suite)

#————生成报告
# with open(r"D:\www\lemon\report\report.html",mode="wb") as save_to_file:
#     one_runner = HTMLTestRunner(stream=save_to_file,
#                    title="这是第一份报告",
#                    verbosity=2,
#                    description="这个报告很重要"
#                    )
#     one_runner.run(one_suite)

#美化中文报告
with open(r"D:\www\lemon\report\report.html",mode="wb") as save_to_file:
    one_runner = HTMLTestReportCN.HTMLTestRunner(stream=save_to_file,
                   title="这是第一份报告",
                   verbosity=2,
                   description="这个报告很重要",
                    tester="隔壁老方"
                   )
    one_runner.run(one_suite)
#美化英文报告
# with open(r"D:\www\lemon\report\report.html",mode="wb") as save_to_file:
#     one_runner = HTMLTestReportEN.HTMLTestRunner(stream=save_to_file,
#                    title="这是第一份报告",
#                    verbosity=2,
#                    description="这个报告很重要",
#                     tester="隔壁老方"
#                    )
#     one_runner.run(one_suite)
#美化带饼状图
# with open(baogao_lujing,mode="wb") as save_to_file:
#     one_runner = HTMLTestRunner_Chart.HTMLTestRunner(stream=save_to_file,
#                    title="这是第一份报告",
#                    verbosity=2,
#                    description="这个报告很重要"
#                    )
#     one_runner.run(one_suite)


# test_reoprt = r'D:\www\lemon\report'
#
# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = test_reoprt + '\\' + now + 'result.html'
# fp = open(filename, 'wb')
# runner = HTMLTestRunner_Chart.HTMLTestRunner(stream=fp,title='这是测试报告', description='用例执行情况：')
# runner.run(one_suite)
# fp.close()

# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
