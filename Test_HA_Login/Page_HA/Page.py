from time import sleep

from selenium.webdriver.common.by import By

# 用户
from Test_HA_Login.Base_HA.test_base_login import Base

username = (By.XPATH, "//input[@placeholder='请输入用户名']")
# 密码
pwd = (By.XPATH, "//input[@placeholder='请输入密码']")
# 验证码
# verify_code = By.CSS_SELECTOR, "#verify_code"
# 登录按钮
login_btn = (By.XPATH, "//div/button")
# 昵称
nick_name = (By.CSS_SELECTOR, "div button span")


class pageLogin(Base):
    #输入用户名
    def __page_username(self,value):
        self.base_input(username,value)

    #输入密码
    def __page_pwd(self,value):
        self.base_input(pwd,value)

    #输入验证码
    # def __page_verify_code(self,value):
    #     self.base_input(verify_code,value)

    # 点击登录按钮
    def __page_login_btn(self):
        self.base_click(login_btn)

    # 获取名称文本
    def page_nick_name(self):
        sleep(2)
        return self.base_text(nick_name)

    def page_login(self, phone, password):
        self.__page_username(phone)
        self.__page_pwd(password)
        # self.__page_verify_code(code)
        self.__page_login_btn()