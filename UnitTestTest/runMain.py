import unittest
import requests
import HTMLTestRunner
import unitTestTest
from datetime import *

# 运行主函数
if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(unitTestTest.suite())
    now = datetime.now()

    report = open("./report/resl_" + now.strftime("%Y%m%d_%H%M%S_%f") + ".html", "wb") # 要先建立report目录，否则会后悔
    runner = HTMLTestRunner.HTMLTestRunner(stream = report, title = u"测试报告", description = u"测试报告详情")
    runner.run(unitTestTest.suite())
    runner.run(unitTestTest.suite2())