

from selenium.webdriver.common.by import By

from PO_test.Base.test_base_login import Base

# 用户
username = (By.CSS_SELECTOR, "#username")
# 密码
pwd = (By.CSS_SELECTOR, "#password")
# print(type(pwd))
# 验证码
verify_code = By.CSS_SELECTOR, "#verify_code"
# print(type(verify_code))
# 登录按钮
login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 昵称
nick_name = By.CSS_SELECTOR, ".userinfo"


class pageLogin(Base):
    #输入用户名
    def __page_username(self,value):
        self.base_input(username,value)

    #输入密码
    def __page_pwd(self,value):
        self.base_input(pwd,value)

    #输入验证码
    def __page_verify_code(self,value):
        self.base_input(verify_code,value)

    # 点击登录按钮
    def __page_login_btn(self):
        self.base_click(login_btn)

    # 获取名称文本
    def page_get_nickname(self):
        self.base_text(nick_name)

    def page_login(self, phone, password, code):
        self.__page_username(phone)
        self.__page_pwd(password)
        self.__page_verify_code(code)
        self.__page_login_btn()