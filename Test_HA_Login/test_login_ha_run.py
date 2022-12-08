import  unittest

from htmltestreport import HTMLTestReport

from Test_HA_Login.Script_HA.test_login import TestLogin

suite = unittest.defaultTestLoader.discover('./Script_HA')
HTMLTestReport('.').run(suite)
# runner = HTMLTestReport('login_test_run.html','登录模块测试')
# runner.run(suite)
# runner = unittest.TextTestRunner()
# runner.run(suite)