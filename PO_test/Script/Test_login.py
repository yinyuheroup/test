import unittest

from PO_test.Page.Page import pageLogin
from PO_test.dirver.dirver import ChromeDirver


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # self.driver = webdriver.Chrome('C:\Users\TEST1\PycharmProjects\pythonProject\Driver\chromedriver.exe')
        # self.driver.maximize_window()
        # self.driver.get('')

        # 封装测试网址打开模块
        self.driver = ChromeDirver('http://192.168.91.130/index.php')
        self.login = pageLogin(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    @parameterized(read_json('login_data', 'login'))
    def test_login(self, phone, password, code, except_text):
        try:
            # 调用登录业务
            self.pageLogin
            nickname = self.login.page_get_nickname
            print(nickname)
            self.assertEqual(nickname, except_text)
        except Exception as e:
            print('错误', e)