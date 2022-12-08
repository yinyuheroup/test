import unittest
from parameterized import parameterized
from login_test.data.build_data import build_data
from login_test.login_demo.login import login


class Test_login(unittest.TestCase):
    @parameterized.expand(build_data())
    def test_login_1(self,username,password,expect):
        self.assertEqual(expect,login(username,password))