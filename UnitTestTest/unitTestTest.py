import unittest
import requests

class LoginTest(unittest.TestCase):
    def setUp(self): # 测试固件，可以将共同的部分提取出来放在这里
        self.url = "http://172.18.11.253/bugfree/Login.php"
    def testlogin1(self):
        """ 登录1测试 """
        # form = {"TestUserName":"111", "TestUserPWD":"111"}
        form = {"xajax":"xCheckUserLogin", "xajaxr":"1574386024465", "xajaxargs[]": "<xjxquery><q>TestUserName=hjwg&TestUserPWD=geee&Language=ZH_CN_UTF-8&HttpRefer=</q></xjxquery>"}
        r = requests.post(self.url, data = form)
       # print(r.status_code)
     #   print(r.text)
        self.assertIn("您的用户名或密码不正确", r.text)

    def testlogin2(self):
        """ 登录2测试 """
            # form = {"TestUserName":"111", "TestUserPWD":"111"}
        form = {"xajax": "xCheckUserLogin", "xajaxr": "1574386024465","xajaxargs[]": "<xjxquery><q>TestUserName=hjwg&TestUserPWD=geee&Language=ZH_CN_UTF-8&HttpRefer=</q></xjxquery>"}
        r = requests.post(self.url, data=form)
     #       print(r.status_code)
        #    print(r.text)
        self.assertIn("您的用户名或密码不正确", r.text)

class LogoutTest(unittest.TestCase):
    def setUp(self): # 测试固件，可以将共同的部分提取出来放在这里
        self.url = "http://172.18.11.253/bugfree/Logout.php?Logout=Yes"
    def testlogout(self):
        """ 退出登录测试 """
        r = requests.get(self.url)
       # print(r.status_code)
      #  print(r.text)
        self.assertIn("Login.php", r.text)

# 测试套件
def suite():
    loginTestCase = unittest.TestSuite()
    loginTestCase.addTest(LoginTest("testlogin1"))
    loginTestCase.addTest(LoginTest("testlogin2"))
    loginTestCase.addTest(LogoutTest("testlogout"))
    return loginTestCase

def suite2():
    loginTestCase = unittest.makeSuite(LoginTest, "testlogin2")  # 将logintest类中的所有testlogin2开头的函数加入到测试套件中
    logoutTestCase = unittest.makeSuite(LogoutTest, "test")
   # alltest = unittest.TestSuite(loginTestCase, logoutTestCase) # 错误写法，无法调用
    alltest = unittest.TestSuite()
    alltest.addTest(loginTestCase)
    alltest.addTest(logoutTestCase)
    return alltest

