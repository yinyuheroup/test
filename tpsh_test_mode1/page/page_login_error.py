# 页面
from tpsh_test_mode1 import page
from tpsh_test_mode1.base.base import Base
from selenium.webdriver.common.by import By

from tpsh_test_mode1.tools.until import Driver_GET


# button_login = By.CSS_SELECTOR, ".red"
# username = By.CSS_SELECTOR, "#username"
# password = By.CSS_SELECTOR, "#password"
# verify_code = By.CSS_SELECTOR, "#verify_code"
# login = By.CSS_SELECTOR,".J-login-submit"
# nick_name = By.CSS_SELECTOR, ".mu-m-phone"

class pageLogin(Base):
    # 填写用户名
    def page_username(self, value):
        self.base_input(page.username, value)

    # 填写密码
    def page_password(self, value):
        self.base_input(page.password, value)

    # 填写验证码
    def page_verify_code(self, value):
        self.base_input(page.verify_code, value)

    # 点击登录,进入登录界面
    def page_click_button(self):
        self.base_click(page.button_login)

    # 点击登录提交按钮
    def page_click_login(self):
        self.base_click(page.login)

    # 点击错误确认按钮
    def page_click_err(self):
        self.base_click(page.login_err_click)

    # 获取文本提供断言
    def page_text(self):
        return self.base_get_text(page.login_err_text)

    # 业务流程
    def page_login_err(self, phone, passwd, code):
        self.page_click_button()
        self.page_username(phone)
        self.page_password(passwd)
        self.page_verify_code(code)
        self.page_click_login()
        self.page_click_err()


if __name__ == '__main__':
    print(page.username)
