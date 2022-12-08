import time
import unittest
from selenium.webdriver.common.by import By
from ..Page_HA.Page import pageLogin
from parameterized import parameterized
from ..dirver_HA.dirver import ChromeDirver
from ..tools.tools import read_json


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # self.driver = webdriver.Chrome(r'C:\Users\TEST1\PycharmProjects\pythonProject\Driver\chromedriver.exe')
        # self.driver.maximize_window()
        # self.driver.get('https://10.12.70.226:9997/zh/login')

        # 封装测试网址打开模块
        self.driver = ChromeDirver('https://10.12.70.226:9997/zh/login')
        self.driver.find_element(By.ID, 'details-button').click()
        self.driver.find_element(By.ID, 'proceed-link').click()
        time.sleep(5)
        self.login = pageLogin(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    @parameterized.expand(read_json('login'))
    # @parameterized.expand([('webadmin', 'webadmin', '开始创建方案')])
    def test01_login(self, phone, password, except_text):
        try:
            # 调用登录业务
            self.login.page_login(phone, password)
            nickname = self.login.page_nick_name()
            print(nickname)
            self.assertEqual(nickname, except_text)
        except Exception as e:
            print('错误', e)

    # def test01_login(self,phone="webadmin",password="webadmin"):
    #     # 调用登录业务
    #     self.login.page_login(phone,password)
    #     # 断言
    #     nickname = self.login.page_nick_name()
    #     print("nickname:", nickname)
