import unittest

from parameterized import parameterized
from tpsh_test_mode1.base.base import Base
from tpsh_test_mode1.page.page_phone import pageLogin
from tpsh_test_mode1.tools.until import Driver_GET, read_json


class test_Tpshop_Login(unittest.TestCase):
    def setUp(self) -> None:
        self.drivers = Driver_GET.get_driver()
        self.web_ele = pageLogin(self.drivers)

    def tearDown(self) -> None:
        self.drivers.quit()
    #手机登录
    @parameterized.expand(read_json('web_login_ok.json', 'login_1'))
    def test_login_phone(self, phone, pwd, code, expect_text):
        print(phone, pwd, code)
        try:
            self.web_ele.page_login(phone, pwd, code)
            # 获取文本
            nickname = self.web_ele.page_text()
            self.assertEqual(expect_text, nickname)
        except Exception as e:
            print("失败:", e)
    # 邮箱登录
    @parameterized.expand(read_json('web_login_ok.json', 'login_2'))
    def test_login_email(self, phone, pwd, code, expect_text):
        print(phone, pwd, code)
        try:
            self.web_ele.page_login(phone, pwd, code)
            # 获取文本
            nickname = self.web_ele.page_text()
            self.assertEqual(expect_text, nickname)
        except Exception as e:
            print("失败:", e)
