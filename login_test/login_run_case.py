import  unittest
from htmltestreport import HTMLTestReport
from login_test.case.login_tase_case import Test_login

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_login))
runner = HTMLTestReport('Login_report.html','登录模块测试报告')
runner.run(suite)