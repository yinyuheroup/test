from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    # 获取元素
    def base_find_element(self, loc, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 填写数据
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 点击按钮
    def base_click(self, loc):
        el = self.base_find_element(loc)
        el.click()

    # 获取文本
    def base_get_text(self, loc):
        # el = self.base_find_element(loc)
        return self.base_find_element(loc).text


