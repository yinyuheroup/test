# def test_login(self, phone, password, code, except_text):
from PO_test.Page.Page import pageLogin

try:
        # 调用登录业务
    pageLogin.page_login(13600001111, 123456, code)
    nickname = self.login.page_get_nickname
    print(nickname)
    assertEqual(nickname, except_text)
except Exception as e:
     print('错误', e)