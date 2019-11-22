import unittest
import requests
import HTMLTestRunner
import unitTestTest


# 运行主函数
if __name__ == '__main__':
    #  runner = unittest.TextTestRunner()
    # runner.run(unitTestTest.suite())
    fr = open("resl.html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream = fr, title = u"测试报告", description = u"详情")
    runner.run(unitTestTest.suite())