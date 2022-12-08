import unittest
from htmltestreport import HTMLTestReport

from case import test_sum
# from case.test_sum import Test_data_sum
from tools.build_data import build_add_data

suite = unittest.TestSuite()
for i in build_add_data():
    suite.addTest(test_sum.Test_data_sum(*i))
# suite = unittest.TestSuite
# runner = unittest.TextTestRunner()
# runner.run(suite)
report = HTMLTestReport('.测试报告.html','test_data')
report.run(suite)